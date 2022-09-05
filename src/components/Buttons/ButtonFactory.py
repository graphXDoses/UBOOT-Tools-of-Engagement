#from kivy.uix.button import Button as PlainBTN
from src.constants.RaobfNames import *
from src.constants.UI import CONTEXT_POOL, not_assigned
from src.constants.Images import IMAGES
from src.constants.EventNames import EVENTS
from src.lib.AppConfig import AppConfig
from src.lib.EventBus import EventBus
from src.components.Buttons.ViewSwitchButton import ViewSwitchButton
from src.components.Buttons.FocusButton import FocusButton
from src.components.Buttons.LinkFocusButton import LinkFocusButton
from src.components.Buttons.ResetButton import ResetButton
from src.components.Buttons.ContextButton import ContextButton

class ButtonFactory:

    def helpContext(self):
        self.buttons = list()

        self.buttons.append(ViewSwitchButton(IMAGES.BUTTONS.HELP))
        self.buttons.append(ContextButton(source=(IMAGES.CONTEXT.FRONT, IMAGES.CONTEXT.BACK)))

        return self.buttons

    def controls(self, context):
        self.buttons = list()
        # breakpoint()
        if context == CONTEXT_POOL.ATTACK_DISC:
            for att, src, role in zip(
                (CR, TG, BALA, ACP),
                (
                    IMAGES.BUTTONS.CR,
                    IMAGES.BUTTONS.TG,
                    IMAGES.BUTTONS.BALA,
                    IMAGES.BUTTONS.ACP
                ),
                (
                    FocusButton,
                    LinkFocusButton,
                    FocusButton,
                    FocusButton
                )
            ):
                self.buttons.append(role(source=src, attachment=att, context=CONTEXT_POOL.ATTACK_DISC))

            activeButton = AppConfig.getInitActiveButton()
            if activeButton == not_assigned:
                self.buttons[-1].setFocus(self.buttons[-1])
            else:
                target = next(filter(lambda i: isinstance(i, (FocusButton, LinkFocusButton)) and i.attachment[0] == activeButton, self.buttons))

                target.setFocus(target)

            self.buttons.append(ResetButton(source=IMAGES.BUTTONS.RESET, context=CONTEXT_POOL.ATTACK_DISC))

        elif context == CONTEXT_POOL.SLIDE_RULE_DISC:
            for att, src, role in zip(
                (DS, TM),
                (
                    IMAGES.BUTTONS.CR,
                    IMAGES.BUTTONS.TG
                ),
                (
                    FocusButton,
                    FocusButton
                )
            ):
                self.buttons.append(role(source=src, attachment=att, context=CONTEXT_POOL.SLIDE_RULE_DISC))

            activeButton = AppConfig.getInitActiveButton()
            if activeButton == not_assigned:
                self.buttons[-1].setFocus(self.buttons[-1])
            else:
                target = next(filter(lambda i: isinstance(i, (FocusButton, LinkFocusButton)) and i.attachment[0] == activeButton, self.buttons))

                target.setFocus(target)

            self.buttons.append(ResetButton(source=IMAGES.BUTTONS.RESET, context=CONTEXT_POOL.SLIDE_RULE_DISC))

        return self.buttons
