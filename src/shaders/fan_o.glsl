// anything before a meaningful section such as this comment are ignored

---VERTEX SHADER--- // vertex shader starts here
#version 300 es

#ifdef GL_ES
precision highp float;
#endif

in vec2 vPosition;
in vec2 vCardinalUv;
in vec2 vTexCoords0;

uniform mat4 projection_mat;

out vec2 tex_coord0;
out vec2 cuv;

void main() {
    tex_coord0 = vTexCoords0;
    cuv = vCardinalUv;
    gl_Position = projection_mat * vec4(vPosition, 0.0, 1.0);
}

---FRAGMENT SHADER--- // fragment shader starts here
#version 300 es

#ifdef GL_ES
precision highp float;
#endif

//varying vec2 tex_coord0;
in vec2 cuv;
out vec4 FragColor;
uniform vec2 iResolution;


const float PI            = 3.14159265359;
// Need Renaming
const vec3 COMP_R_COL     = vec3(0.7412, 0.7020, 0.6039);
const vec3 REL_B_COL      = vec3(0.2706, 0.1882, 0.2039);
const vec3 REL_B_GRAY_COL = vec3(0.6784, 0.6510, 0.6667);
////////////////////////////////////////////////////////
const vec3 InkLightOrange = vec3(0.7961, 0.6745, 0.5373);
const vec3 InkLightBlue   = vec3(0.2627, 0.2902, 0.3529);


const vec3 SidesColors[3] = vec3[3](
    vec3(0.0000, 0.0000, 0.0000),
    vec3(0.6118, 0.0000, 0.0000),
    vec3(0.1608, 0.5843, 0.2588)
);


const vec3 Knob = vec3(0.6627, 0.6627, 0.6627);

#define bake(sdf) 1. - smoothstep(-fwidth(sdf)*.8, fwidth(sdf)*.8, sdf)
#define dot2(v) dot(v, v)
#define radians(a) a / 180. * PI

vec2 fan(in vec2 pos, in float q)
{
    q = radians(q);
    float ang = atan(pos.x, pos.y),
    len = length(pos.xy);
    ang = mod(ang + q/2., q) - q/2.;
    pos.xy = len * vec2(sin(ang), cos(ang));
    return pos;
}

float circle(vec2 cs)
{
    return length(cs);
}

float sdBox( in vec2 p, in vec2 b )
{
    vec2 d = abs(p)-b;
    return length(max(d,0.0)) + min(max(d.x,d.y),0.0);
}

float sdUnevenCapsule( vec2 p, float r1, float r2, float h )
{
    p.x = abs(p.x);
    float b = (r1-r2)/h;
    float a = sqrt(1.0-b*b);
    float k = dot(p,vec2(-b,a));
    if( k < 0.0 ) return length(p) - r1;
    if( k > a*h ) return length(p-vec2(0.0,h)) - r2;
    return dot(p, vec2(a,b) ) - r1;
}

float triangle(vec2 cs, vec2 pos, vec2 size, float fac)
{
    float sdf = smoothstep(((cs.y-pos.y)*size.x) - fac, ((cs.y-pos.y)*size.x) + fac, abs(cs.x));
    sdf += smoothstep(size.y - fac, size.y + fac, cs.y-pos.y);
    return max(1. - sdf, 0.);
}

float triangle( in vec2 p, in vec2 q )
{
    p.x = abs(p.x);
    vec2 a = p - q*clamp( dot(p,q)/dot(q,q), 0.0, 1.0 );
    vec2 b = p - q*vec2( clamp( p.x/q.x, 0.0, 1.0 ), 1.0 );
    float s = -sign( q.y );
    vec2 d = min( vec2( dot(a,a), s*(p.x*q.y-p.y*q.x) ),
                  vec2( dot(b,b), s*(p.y-q.y)  ));
    return -sqrt(d.x)*sign(d.y);
}

float line( in vec2 p, in vec2 a, in vec2 b, float width, float fac )
{
    vec2 pa = p-a, ba = b-a;
    float h = clamp( dot(pa,ba)/dot(ba,ba), 0., 1.0 );
    return smoothstep(width - fac, width + fac, length( pa - ba*h ));
}

float line( in vec2 p, in vec2 a, in vec2 b)
{
    vec2 pa = p-a, ba = b-a;
    float h = clamp( dot(pa,ba)/dot(ba,ba), 0., 1.0 );
    return length( pa - ba*h );
}

float sdTrapezoid( in vec2 p, in float r1, float r2, float he )
{
    vec2 k1 = vec2(r2,he);
    vec2 k2 = vec2(r2-r1,2.0*he);
    p.x = abs(p.x);
    vec2 ca = vec2(p.x-min(p.x,(p.y<0.0)?r1:r2), abs(p.y)-he);
    vec2 cb = p - k1 + k2*clamp( dot(k1-p,k2)/dot2(k2), 0.0, 1.0 );
    float s = (cb.x<0.0 && ca.y<0.0) ? -1.0 : 1.0;
    return s*sqrt( min(dot2(ca),dot2(cb)) );
}

float smin(float a, float b, float k) {
    float h = clamp(0.5 + 0.5*(a-b)/k, 0.0, 1.0);
    return mix(a, b, h) - k*h*(1.0-h);
}

float sdPie( in vec2 p, in vec2 c, in float r )
{
    p.x = abs(p.x);
    float l = length(p) - r;
    float m = length(p-c*clamp(dot(p,c),0.0,r)); // c=sin/cos of aperture
    return max(l,m*sign(c.y*p.x-c.x*p.y));
}

float sdEgg( in vec2 p, in float ra, in float rb )
{
    const float k = sqrt(3.0);
    p.x = abs(p.x);
    float r = ra - rb;
    return ((p.y<0.0)       ? length(vec2(p.x,  p.y    )) - r :
            (k*(p.x+r)<p.y) ? length(vec2(p.x,  p.y-k*r)) :
                              length(vec2(p.x+r,p.y    )) - 2.0*r) - rb;
}

mat2 rotationMatrix(float angle) {
	float c = cos(angle), s = sin(angle);
    return mat2(
        c, -s,
        s,  c
    );
}

void main()
{
    vec2 fc = gl_FragCoord.xy;
    float minimum_dim = min(iResolution.x, iResolution.y);
    float maximum_dim = max(iResolution.x, iResolution.y);
    vec2 uv = (fc.xy - .5*iResolution.xy)/maximum_dim;
    float sc = maximum_dim / minimum_dim *2.*1.77;
    //sc *= 2.75;

    float yo = 0.;
    sc -= clamp(yo, 0., 2.5);
    uv *= sc;

    vec2 p = fan(uv, 360./360.);

    vec2 go = fan(uv, 360./36.);

    vec2 fo = fan(uv*rotationMatrix(PI/36.), (360./36.));

    // Outter Disc Entities

    float b = 1. - line(p,vec2(0.,1.602), vec2(0., 1.453), 0.003, (1./maximum_dim) * sc);

    float b2 = 1. - line(go,vec2(0.,1.662), vec2(0., 1.453), 0.005, (1./maximum_dim) * sc);

    float b3 = 1. - line(fo,vec2(0.,1.652), vec2(0., 1.453), 0.005, (1./maximum_dim) * sc);

    /////////////////////////////////////////////////////////////////////////////////////////

    // Middle Disc Entities

    float c = 1. - line(p,vec2(0.,1.36), vec2(0., 1.247), 0.002, (1./maximum_dim) * sc);
    float gc = 1. - line(p,vec2(0.,1.080), vec2(0., 1.059), 0.002, (1./maximum_dim) * sc);

    float c2 = 1. - line(go,vec2(0.,1.36), vec2(0., 1.179), 0.003, (1./maximum_dim) * sc);
    float gc2 = 1. - line(go,vec2(0.,1.080), vec2(0., 1.012), 0.003, (1./maximum_dim) * sc);

    float c3 = 1. - line(fo,vec2(0.,1.36), vec2(0., 1.204), 0.002, (1./maximum_dim) * sc);
    float gc3 = 1. - line(fo,vec2(0.,1.080), vec2(0., 1.036), 0.002, (1./maximum_dim) * sc);

    float sdfNorth = sdPie(uv, vec2(sin(radians(5.)), cos(radians(5.))), 1.37);
    float mskNorth = bake(sdfNorth);

    c2 *= 1. - mskNorth;

    float c2North = line(uv, vec2(0.,1.36), vec2(0., 1.179))+37e-4;
    float triNorth = triangle(uv-vec2(0., 1.196), vec2(0.6, -0.75)*0.17);
    triNorth = min(triNorth, c2North);
    triNorth = bake(abs(triNorth)-7e-3);
    triNorth *= smoothstep(-fwidth((length(uv)-1.080)), fwidth((length(uv)-1.080)), (length(uv)-1.080));

    /////////////////////////////////////////////////////////////////////////////////////////

    float h   = circle(go - vec2(0., 1.179)) - 0.010;
    h   = bake(h);
    float gh  = circle(go - vec2(0., 1.012)) - 0.009;
    gh  = bake(gh);
    float h2  = circle(fo - vec2(0., 1.204)) - 0.010;
    h2  = bake(h2);
    float gh2 = circle(fo - vec2(0., 1.036)) - 0.009;
    gh2 = bake(gh2);

    h *= 1. - mskNorth;

    /////////////////////////////////////////////////////////////////////////////////////////

    float tr = triangle(uv, vec2(0., 1.364), vec2(0.467, 0.08), (1./maximum_dim)*sc);
    //tr -= step(0.08, uv.y);

    float bigO = circle(uv - vec2(0.)) - 1.77;
    bigO = bake(bigO);
    float midO = circle(uv - vec2(0.)) - 1.363;
    float miscDiscLOrange = circle(uv - vec2(0.)) - 0.746;
    miscDiscLOrange = bake(miscDiscLOrange);
    float miscDiscLBlue = circle(uv - vec2(0.)) - 0.53;
    miscDiscLBlue = bake(miscDiscLBlue);
    float miscDiscBlack = circle(uv - vec2(0.)) - 0.244;
    miscDiscBlack = bake(miscDiscBlack);
    float td = circle(uv - vec2(0.)) - 0.907;
    td = bake(td);

    // Inner Disc Entities

    float d = 1. - line(p,vec2(0.,0.907), vec2(0., 0.862), 0.002, (1./maximum_dim) * sc);
    float gd = 1. - line(p,vec2(0.,0.637), vec2(0., 0.607), 0.002, (1./maximum_dim) * sc);

    float d2 = 1. - line(go,vec2(0.,0.907), vec2(0., 0.84), 0.003, (1./maximum_dim) * sc);
    float gd2 = 1. - line(go,vec2(0.,0.637), vec2(0., 0.591), 0.003, (1./maximum_dim) * sc);

    float d3 = 1. - line(fo,vec2(0.,0.907), vec2(0., 0.848), 0.003, (1./maximum_dim) * sc);
    float gd3 = 1. - line(fo,vec2(0.,0.637), vec2(0., 0.597), 0.003, (1./maximum_dim) * sc);

    /////////////////////////////////////////////////////////////////////////////////////////

    float he = 1.373;
    float offset = 0.2;

    // Pointer for bala
    float pointer = sdTrapezoid(uv-vec2(0., (he/2.)+offset), 0.1995, 0.065, (he/2.)-offset);

    float fac = 0.04;

    float pie = sdPie(uv-vec2(0., fac*0.), vec2(sin(radians(61.)), cos(radians(61.))), 0.61);
    pie -= fac;
    float pieMask = sdPie(uv-vec2(0., fac*.0), vec2(sin(radians(60.5)), cos(radians(60.5))), 0.65);
    pieMask = bake(pieMask);

    gd  *= pieMask;
    gd2 *= pieMask;
    gd3 *= pieMask;

    float bala = smin(
        pointer,
        pie,
        fac
    );

    ////////////////////////////////////////////////////////////////////////////////////////

    // he for acp
    he = 1.602;

    // Pointer for acp
    vec2 tuv = uv;
    tuv.y = abs(tuv.y);
    pointer = sdTrapezoid(tuv-vec2(0., (he/2.)-6e-2), 0.1995, 0.065, (he/2.));


    float acp = pointer;

    float Bship = sdEgg(uv-vec2(0., 0.472), 0.06, -0.06*(4.25*2.)+0.1);
    tuv = uv;
    tuv.y = 1. - tuv.y;
    Bship = min(Bship, sdUnevenCapsule(tuv-vec2(0., 1.-0.472), 0.06, 0.04, .5));
    Bship = max(Bship, sdBox(uv-vec2(0., 0.5), vec2(0.12, 0.25)));

    float Bship2 = sdEgg(uv+vec2(0., 0.5), 0.06, -0.06*(4.25*2.)+0.1);
    Bship2 = min(Bship2, sdUnevenCapsule(tuv-vec2(0., (2.-0.5)*1.), 0.06, 0.04, .5));
    Bship2 = max(Bship2, sdBox(uv+vec2(0., 0.472), vec2(0.12, 0.25)));

    Bship = min(Bship, Bship2);

    Bship = bake(abs(Bship)-3e-3);

    tuv = uv;
    tuv.x = abs(tuv.x);

    float arrows = line(tuv, vec2(0.244, 0.), vec2(0.746-5e-3, 0.))-5e-3;

    tuv = uv;
    tuv = abs(tuv);

    pointer = line(tuv, vec2(0.746-5e-3, 0.), vec2(0.715, 0.018))-5e-3;
    arrows = min(arrows, pointer);

    arrows = bake(arrows);

    bala = smin(
        line(uv, vec2(0.), vec2(0., 0.2))-0.13,
        bala,
        7e-3
    );

    bala = max(bala, midO);
    acp = max(acp, length(uv)-(he-9e-2));

    float tmp = 1. - smoothstep(20e-3, -25e-3, bala);

    bala = bake(bala);

    bala *= tmp;

    tmp = 1. - smoothstep(20e-3, -25e-3, acp);
    acp  = bake(acp);
    acp  *= tmp;
    //acp = tmp;

    midO = bake(midO);

    // Color each side

    tuv = uv;
    tuv.y = abs(tuv.y);

    float j = 0.;
    j = sdPie(tuv, vec2(sin(radians(0.3)), cos(radians(0.3))), 1.77);
    j = step(0., j);
    j *= 1. + (1. * step(0., tuv.x));
    j = floor(j);

    pointer = length(uv)-0.115;
    pointer = bake(pointer);

    ////////////////////////////////////////////////////////////////////////////

    float x = max(b, b2);
    x = max(x, b3);

    float y = max(c, c2);
    y = max(y, c3);
    y = max(y, h);
    y = max(y, h2);
    y = max(y, gc);
    y = max(y, gc2);
    y = max(y, gc3);
    y = max(y, gh);
    y = max(y, gh2);

    float z = max(d, d2);
    z = max(z, d3);
    z = max(z, gd);
    z = max(z, gd2);
    z = max(z, gd3);

    vec3 col = vec3(0.);
    col = mix(col, REL_B_COL, bigO);
    col = mix(col, REL_B_GRAY_COL, x);
    col = mix(col, REL_B_GRAY_COL, tr);
    col = mix(col, COMP_R_COL, midO);
    col = mix(col, SidesColors[0], y);
    col = mix(col, vec3(1.), td);
    col = mix(col, InkLightOrange, miscDiscLOrange);
    col = mix(col, InkLightBlue, miscDiscLBlue);
    col = mix(col, SidesColors[int(j)], arrows);
    col = mix(col, vec3(1.), Bship);
    col = mix(col, SidesColors[int(j)], z);
    col = mix(col, SidesColors[0], miscDiscBlack);
    col = mix(col, Knob, pointer);

    col = mix(col, vec3(0.1), bala);
    col = mix(col, vec3(0.1), acp);

    col = mix(col, SidesColors[0], triNorth);

    //col = vec3(j);

    // Output to screen
    FragColor = vec4(col,1.0);
}
