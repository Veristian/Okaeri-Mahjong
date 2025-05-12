define kotoha = Character("Kotoha", color="#c8ffc8")
define kirino = Character("Kirino", color="#c8c8ff")
define sara = Character("Sara", color="#ffc8c8")
define miko = Character("Miko", color="#ffffc8")
define slightleft = Position(xalign=0.2, yalign=0.5)
define slightright = Position(xalign=0.8, yalign=0.5)     

init python:

    import random

    class SparkleParticle:
        def __init__(self, x, y):
            self.x = x + random.uniform(-20, 20)
            self.y = y + random.uniform(-20, 20)
            self.alpha = 255
            self.size = random.uniform(0.3, 1.0)
            self.lifetime = random.uniform(0.4, 0.8)  # seconds

        def update(self, dtime):
            self.alpha -= 255 * dtime / self.lifetime
            return self.alpha > 0

    class MouseSparkleDisplayable(renpy.Displayable):
        def __init__(self):
            super(MouseSparkleDisplayable, self).__init__()
            self.particles = []
            self.oldst = None
            self.sparkle_img = Image("sparkle.png")

        def visit(self):
            return [ self.sparkle_img ]

        def render(self, width, height, st, at):
            r = renpy.Render(width, height)

            if self.oldst is None:
                self.oldst = st
            dtime = st - self.oldst
            self.oldst = st

            # Get current mouse position
            mouse_pos = renpy.get_mouse_pos()
            if mouse_pos is not None:
                mx, my = mouse_pos
                # Spawn a few particles at the mouse position
                for _ in range(3):
                    self.particles.append(SparkleParticle(mx, my))

            # Render particles
            new_particles = []
            from renpy.display.transform import Transform

            # Inside your render() method:
            for p in self.particles:
                if p.update(dtime):
                    sparkle = Transform(self.sparkle_img, alpha=p.alpha, zoom=p.size)
                    sparkle_render = renpy.render(sparkle, width, height, st, at)
                    r.blit(sparkle_render, (int(p.x), int(p.y)))
                    new_particles.append(p)

            self.particles = new_particles

            # Schedule next redraw
            renpy.redraw(self, 0.01)
            return r

screen sparkles():
    add MouseSparkleDisplayable()

label start:
    
    scene bg_classroom with dissolve
    show screen sparkles
    "It's almost the end of lunch break."
    "After finishing my lunch, I walked slowly towards my own classroom."


    "When I enter the classroom, I see my classmate — Shikihara Kirino — playing digital mahjong."
    "As I watched her play, a flashback of my past memories came back to me."
    "I used to play mahjong with my family."
    "We would always play mahjong in the evening."
    "But as I grew better in the game, the more they hate playing with me."
    "One of the reasons is because they can't enjoy the game if I kept on winning."
    "Since then, I started to hate mahjong."

    "When I realised it, she already had 1 melded triplet and 1 melded sequence"
    "I analyze her hand and her wait tiles."

    show kotoha sad at slightleft
    kotoha "..."

    "Then I noticed something — She has no winning pattern."

    kotoha "No Yaku.."

    show kirino shock at slightright
    kirino "Hmm?"

    "Soon, Kirino got her last waiting hand."

    show kirino happy at slightright
    kirino "Ah.. finally, my hand is complete."
    kirino "..."

    show kotoha neutral at slightleft
    kotoha "..."

    show kirino shock at slightright
    kirino "Eh? It really is No Yaku!"
    kirino "How do you know if it is going to be no yaku?"

    show kotoha sad at slightleft
    kotoha "Well.."
    kotoha "I used to play mahjong before."

    show kirino happy at slightright
    kirino "Ohh!!"
    kirino "Then.. Do you want to play?"

    show kotoha sad at slightleft
    kotoha "I.. Don't.."

    show kirino shock at slightright
    kirino "Ehh-- Why? Even though you are good at it?"

    kotoha "That's a different story.."
    kotoha "I just.. can't enjoy Mahjong."

    show kirino happy at slightright
    kirino "Ehh-- Come on!"
    kirino "If I remember, your name is Takanashi Kotoha slightright?"

    show kotoha neutral at slightleft
    kotoha "Well.. yeah.."

    kirino "Then Come on Kotoha!"

    kotoha "She instantly calls me by my first name?"

    kotoha "I can't, Shikihara.."

    kirino "Just call me Kirino!"

    show kotoha sad at slightleft
    kotoha "Well.. I can't.. Kirino."

    show kirino shock at slightright
    kirino "I'm begging you Kotoha!"

    "This girl is so persistent!"

    kotoha "Fine.."
    kotoha "But just one game okay?"

    show kirino happy at slightright
    kirino "Yes!"
    kirino "Let's go to the Mahjong Club Room after school later!"

    "Sigh.. I give up.."

    scene bg_classroom with fade

    "*After School*"
    "Just slightright after the end of the last class, Kirino instantly stood up from her seat."
    "In an instant, she approaches my seat."

    show kirino happy at slightright
    kirino "Kotoha!"

    show kotoha neutral at slightleft
    kotoha "Alslightright.. Alslightright.."

    "We slightleft our classroom, and started to head to the clubroom."

    scene bg_clubroom with fade

    "Once we reached our destination, Kirino opens the door."
    "Ah.. there is a person inside."

    show sara neutral at center
    kirino "President! We're here!"

    "She was drinking her tea while looking outside through the window."
    "When she heard Kirino's voice, she looked at our direction."

    sara "Ah, Kirino!"
    sara "And.. who would that person be?"

    show kotoha neutral at slightleft
    kotoha "My name is Takanashi Kotoha."

    kirino "I invited Kotoha here to play mahjong."

    sara "Kirino, I thought you know about our situation slightright now."
    sara "We don't have enough members to play Mahjong."

    kirino "But I remember we can do a 3-player Mahjong."

    sara "Hmm.. I see.."

    kirino "Ah, sorry for the late introduction."
    kirino "Kotoha, She is the president of the Mahjong Club — Kashiwazaki Sara."

    sara "I'm Sara."
    sara "So, are we doing 3-player Mahjong?"

    kirino "Yes!"

    sara "Alslightright then, let's set it u—"

    "*SLAM*"

    show miko shock at slightright
    miko "WAIT!"

    show sara shock at center
    sara "Hmm??"

    miko "I've heard everything!"
    miko "And you shall all be grateful!"
    miko "Because I, Igarashi Miko, shall be the fourth player!"

    show sara happy at center
    sara "Oh my, another girl came"
    sara "This might be interesting."
    sara "Alslightright then, join us Miko."

    show kirino shock at slightright
    kirino "Ehh-- are we really playing with her?"

    sara "The more the merrier, slightright Kotoha?"

    show kotoha neutral at slightleft
    kotoha "Yeah..."

    kirino "Ehh-- fine.."

    show miko happy at slightright
    miko "hmph hmph.. I will show you all how strong I am!"

    sara "Alslightright everyone, let's start setting up the game."

    "We shuffled through the Mahjong tiles, before eventually setting everything up."

    scene bg_mahjong_table with fade

    "East 1"
    "My hand: 5 5 7m 5 5p a 6 7 8 9p 2s 9s 4 6z"
    "My hand looks solid for a starting hand."
    "I think I can just aim for Tanyao (All Simple)."
    "Especially with 2 red doras with me."

    "East 1, Turn 2, Kotoha's turn"
    "Hand: 1 2 5 5 7m 5 5p d 6 7 8 9p 2 9s"
    "Oh, I got a 3 pin."
    "Let's throw a 9 sou."
    "*Discards 9s*"

    show miko happy at slightright
    miko "Pon!"

    kotoha "Eh? Open triplet on a terminal tile?"
    kotoha "What is this girl planning?"

    "Turn 3"
    "Draws 6m"
    "Discards 2s"

    miko "Pon!"

    kotoha "I see, so she is planning to go for Toitoi (All Triplets)."

    "Turn 7"
    "My hand is ready now."
    "Wait for either 1p or 4p."

    "Miko has gotten 3 open triplets."
    "And it's not the same suit."
    "For Kirino, her discards look weird."
    "As for the president.. very suspicious."

    "Only one 1p and 4p discarded each."
    "Let's call a Riichi."

    show kotoha neutral at slightleft
    kotoha "Riichi!"
    "*Discards 9p*"

    "Turn 13, Miko's turn"
    "Miko discards 2p"
    "Draws 7m"
    "*Discards 7m*"

    "Sara discards 9p"

    show kirino happy at slightright
    kirino "Oh finally!"
    kirino "Riichi!"
    "*Discards 8p*"

    kotoha "Eh? Riichi slightright now?"
    "But considering that she is a beginner, I don't think she knows my wait."
    "Let's see it in the end."

    "Turn 15, Kirino draws and discards 4p"

    kotoha "Ron!"

    show kirino shock at slightright
    kirino "Ehh--"

    kotoha "Riichi, Tanyao (All Simple), Red Dora 2."
    kotoha "8000 points."

    kirino "Ehh-- that's too much!"

    show miko sad at slightright
    miko "Ahh.. just a little more.."

    "*Kirino gives Kotoha 8000 points.*"

    kotoha "That should do for now.."
    kotoha "I hope nothing bad will happen to me after this."

    show sara happy at center
    sara "Ahh~ too bad."

    return
