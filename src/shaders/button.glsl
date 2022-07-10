// anything before a meaningful section such as this comment are ignored

---VERTEX SHADER--- // vertex shader starts here
#ifdef GL_ES
precision highp float;
#endif

attribute vec2 vPosition;
attribute vec2 vCardinalUv;
attribute vec2 vTexCoords0;

uniform mat4 projection_mat;

varying vec2 tex_coord0;
varying vec2 uv;

void main() {
    tex_coord0 = vTexCoords0;
    uv = vCardinalUv;
    gl_Position = projection_mat * vec4(vPosition, 0.0, 1.0);
}

---FRAGMENT SHADER--- // fragment shader starts here
#ifdef GL_ES
precision highp float;
#endif

varying vec2 tex_coord0;
varying vec2 uv;
uniform sampler2D texture0;
uniform float hasFocus;
uniform vec3 bg_color_norm;
uniform vec3 bg_color_on;

void main() {

    vec2 muv = uv - vec2(0.5);
    float d = length(muv);
    float r = 0.5;
    float c_out = smoothstep(r, r-0.02, d);
    r -= 0.075;
    float c_in = smoothstep(r, r+0.02, d);

    vec3 bg_on = vec3(c_out) * bg_color_on;
    vec3 bg_off = vec3(min(c_in, c_out)) * bg_color_norm;
    vec3 bg = mix(bg_on, bg_off, 1.0-hasFocus);

    vec3 icon_on  = vec3(texture2D(texture0, tex_coord0).a);
    vec3 icon_off = vec3(texture2D(texture0, tex_coord0).a) * bg_color_norm;
    vec3 icon = mix(icon_on, icon_off, 1.0-hasFocus);

    vec3 color = max(bg, icon);

    gl_FragColor = vec4(color, 1);
}
