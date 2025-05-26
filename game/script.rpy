
#This file contains all the custom code
init python:
    particleAmount = 2
    import random

    class SparkleParticle:
        def __init__(self, x, y):
            self.x = x + random.uniform(-20, 20)
            self.y = y + random.uniform(-20, 20)
            self.alpha = 255
            self.size = random.uniform(0.3, 1.0)*0.1
            self.lifetime = random.uniform(0.4, 0.8)  # seconds

        def update(self, dtime):
            self.alpha -= 255 * dtime / self.lifetime
            self.size = self.size * (1 - dtime / self.lifetime)
            self.x += random.uniform(-1, 1) * dtime * 100
            self.y += random.uniform(0, 1) * dtime * 300
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
                for _ in range(particleAmount):
                    self.particles.append(SparkleParticle(mx, my))

            # Render particles
            new_particles = []
            from renpy.display.transform import Transform

            for p in self.particles:
                if p.update(dtime):
                    sparkle = Transform(self.sparkle_img, alpha=p.alpha, zoom=p.size)
                    sparkle_render = renpy.render(sparkle, width, height, st, at)
                    r.blit(sparkle_render, (int(p.x), int(p.y)))
                    new_particles.append(p)

            self.particles = new_particles

            # Schedule next redraw
            renpy.redraw(self, 1/renpy.get_refresh_rate())
            return r



    import random
    import pygame
    import math
    from renpy.display.image import Image
    from renpy.display.transform import Transform

    clickparticleAmount = 20

    class ClickParticle:
        def __init__(self, x, y):
            angle = random.uniform(0, 2 * 3.14159)  # Random direction
            speed = random.uniform(150, 400) * 5        # Fast outward burst

            self.vx = speed * math.cos(angle)
            self.vy = speed * math.sin(angle)

            self.x = x
            self.y = y
            self.alpha = 255
            self.size = random.uniform(0.3, 1.0) * 0.05
            self.lifetime = random.uniform(0.4, 0.8)
            self.age = 0.0

        def update(self, dtime):
            self.age += dtime
            if self.age >= self.lifetime:
                return False

            # Fade and shrink over time
            self.alpha = 255 * (1 - self.age / self.lifetime)
            self.size *= (1 - dtime / self.lifetime)

            # Move outward
            self.x += self.vx * dtime
            self.y += self.vy * dtime

            return True


    class MouseClickDisplayable(renpy.Displayable):
        def __init__(self):
            super(MouseClickDisplayable, self).__init__()
            self.particles = []
            self.pending_clicks = []
            self.oldst = None
            self.sparkle_img = Image("sparkle.png")

        def visit(self):
            return [self.sparkle_img]

        def render(self, width, height, st, at):
            r = renpy.Render(width, height)

            if self.oldst is None:
                self.oldst = st
            dtime = st - self.oldst
            self.oldst = st

            # Add new particles from clicks
            for mx, my in self.pending_clicks:
                for _ in range(clickparticleAmount):
                    self.particles.append(ClickParticle(mx, my))
            self.pending_clicks = []

            # Update and render particles
            new_particles = []
            for p in self.particles:
                if p.update(dtime):
                    tr = Transform(self.sparkle_img, alpha=p.alpha, zoom=p.size)
                    spr = renpy.render(tr, width, height, st, at)
                    r.blit(spr, (int(p.x), int(p.y)))
                    new_particles.append(p)
            self.particles = new_particles

            # 🔥 Always redraw if particles still exist
            # if self.particles:
            renpy.redraw(self, 1 / renpy.get_refresh_rate())
            return r


        def event(self, ev, x, y, st):
            # On left click, queue one burst:
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.pending_clicks.append((x, y))

    




transform slightleft:
    xalign -0.5
    yalign 0.1
transform slightright:
    xalign 1.5
    yalign 0.1 
transform centerright:
    xalign 0.8
    yalign 0.1
transform centerleft:
    xalign 0.2
    yalign 0.1

#numbers
image 1m = AlphaMask("row-1-column-1","Mask.png")
image 2m = AlphaMask("row-1-column-2","Mask.png")
image 3m = AlphaMask("row-1-column-3","Mask.png")
image 4m = AlphaMask("row-1-column-4","Mask.png")
image 5m = AlphaMask("row-1-column-5","Mask.png")
image 0m = AlphaMask("row-1-column-6","Mask.png")
image 6m = AlphaMask("row-1-column-7","Mask.png")
image 7m = AlphaMask("row-1-column-8","Mask.png")
image 8m = AlphaMask("row-1-column-9","Mask.png")
image 9m = AlphaMask("row-1-column-10","Mask.png")

#balls
image 1p = AlphaMask("row-2-column-1","Mask.png")
image 2p = AlphaMask("row-2-column-2","Mask.png")
image 3p = AlphaMask("row-2-column-3","Mask.png")
image 4p = AlphaMask("row-2-column-4","Mask.png")
image 5p = AlphaMask("row-2-column-5","Mask.png")
image 0p = AlphaMask("row-2-column-6","Mask.png")
image 6p = AlphaMask("row-2-column-7","Mask.png")
image 7p = AlphaMask("row-2-column-8","Mask.png")
image 8p = AlphaMask("row-2-column-9","Mask.png")
image 9p = AlphaMask("row-2-column-10","Mask.png")

#bamboo
image 1s = AlphaMask("row-3-column-1","Mask.png")
image 2s = AlphaMask("row-3-column-2","Mask.png")
image 3s = AlphaMask("row-3-column-3","Mask.png")
image 4s = AlphaMask("row-3-column-4","Mask.png")
image 5s = AlphaMask("row-3-column-5","Mask.png")
image 0s = AlphaMask("row-3-column-6","Mask.png")
image 6s = AlphaMask("row-3-column-7","Mask.png")
image 7s = AlphaMask("row-3-column-8","Mask.png")
image 8s = AlphaMask("row-3-column-9","Mask.png")
image 9s = AlphaMask("row-3-column-10","Mask.png")


#wind
image 1z = AlphaMask("row-4-column-1","Mask.png")
image 2z = AlphaMask("row-4-column-2","Mask.png")
image 3z = AlphaMask("row-4-column-3","Mask.png")
image 4z = AlphaMask("row-4-column-4","Mask.png")

#dragon
image 5z = AlphaMask("row-4-column-6","Mask.png")
image 6z = AlphaMask("row-4-column-5","Mask.png")
image 7z = AlphaMask("row-4-column-7","Mask.png")


transform tile_transform:
    left
    zoom 0.8
    


screen sparkles():
    add MouseSparkleDisplayable()
    add MouseClickDisplayable()



define Kotoha = Character("Kotoha", color="#c8ffc8")
define Kirino = Character("Kirino", color="#c8c8ff")
define Sara = Character("Sara", color="#ffc8c8")
define Miko = Character("Miko", color="#ffffc8")

# Then define images for each expression
image Kotoha Neutral = "Kotoha.png"
image Kotoha Happy = "Kotoha_Happy.png"
image Kotoha Surprised = "Kotoha_Surprised.png"
image Kotoha Sad = "Kotoha_Sad.png"

image Kirino Neutral = "Kirino_Default.png"
image Kirino Happy = "Kirino_Happy.png"
image Kirino Surprised = "Kirino_Surprised.png"
image Kirino Sad = "Kirino_Sad.png"

image Sara Neutral = "Sara.png"
image Sara Happy = "Sara_Happy.png"
image Sara Surprised = "Sara_Surprised.png"
image Sara Sad = "Sara_Sad.png"

image Miko Neutral = "Miko_Default.png"
image Miko Happy = "Miko_Happy.png"
image Miko Surprised = "Miko_Surprised.png"
image Miko Sad = "Miko_Sad.png"

image hand v1 = Composite(
    (0.5 ,0.5),
    (0, 0), "5m",
    (150, 0), "5m",
    (300, 0), "7m",
    (450, 0), "0p",
    (600, 0), "0p",
    (750, 0), "6p",
    (900, 0), "7p",
    (1050, 0), "8p",
    (1200, 0), "9p",
    (1350, 0), "2s",
    (1500, 0), "9s",
    (1650, 0), "4z",
    (1800, 0), "6z",
)



label start:

    scene bg hallway with dissolve

    show screen sparkles

    play music 'audio/sakura.mp3'

    "It's almost the end of lunch break."
    "After finishing my lunch, I walked slowly towards my own classroom."
    
    scene bg classroom with dissolve

    "When I entered the classroom, I saw my classmate — Kirino — playing digital mahjong."
    "As I watched her play, a flashback of my past memories came back to me."
    "I used to play mahjong with my family."
    "We would always play mahjong in the evening."
    "But as I grew better in the game, the more they hated playing with me."
    "One of the reasons is because they couldn't enjoy the game if I kept on winning."
    "Since then, I started to hate mahjong."
    "When I realized it, she already had 1 melded triplet and 1 melded sequence."
    "I analyze her hand and her wait tiles."

    show Kotoha Sad at slightleft 
    Kotoha "..."

    "Then I noticed something — She has no winning pattern."

    Kotoha "No Yaku.."

    "I accidentally blurted it out."

    show Kirino Surprised at slightright
    Kirino "Hmm?"

    Kirino "What do you mean 'No Yaku'?"

    "Soon, Kirino got her last waiting hand."

    show Kirino Happy
    Kirino "Ah.. finally, my hand is complete."
    Kirino "..."

    show Kotoha Neutral
    Kotoha "..."

    show Kirino Surprised
    Kirino "Eh? It really is No Yaku!"
    Kirino "How do you know if it is going to be no yaku?"

    show Kotoha Sad
    Kotoha "Well.."

    show Kotoha Neutral

    Kotoha "I used to play mahjong before."

    show Kirino Happy 
    Kirino "Ohh!"
    Kirino "Then.. Do you want to play?"

    show Kotoha Sad 
    Kotoha "I.. Don't.."

    Kirino "Ehh-- Why? Even though you are good at it?"

    Kotoha "That's a different story.."
    Kotoha "I just.. can't enjoy Mahjong."

    Kirino "Ehh-- Come on!"
    Kirino "If I remember, your name is Kotoha right?"

    Kotoha "Well.. yeah.."

    Kirino "Then come on Kotoha!"

    "She instantly calls me by my first name?"

    Kotoha "I can't, Shikihara.."

    Kirino "Just call me Kirino!"

    Kotoha "Well.. I can't.. Kirino."

    Kirino "I'm begging you Kotoha!"

    "This girl is so persistent!"
    "Fine.. I'll just follow her, then leave once after one game"

    show Kotoha Neutral

    Kotoha "Fine.."
    Kotoha "But just one game okay?"

    Kirino "Yes!"
    Kirino "Let's go to the Mahjong Club Room after school later!"

    show Kotoha Sad

    "Sigh.. I give up.."

    # After school scene
    scene bg hallway with dissolve
    show screen sparkles

    "*After School*"
    "Just right after the end of the last class, Kirino instantly stood up from her seat."
    "In an instant, She approaches my seat."

    show Kirino Happy at slightright
    Kirino "Kotoha!"

    show Kotoha Neutral at slightleft
    Kotoha "Alright.. alright.."

    "We left our classroom, and started to head to the clubroom."
    "Once we've reached our destination, Kirino opens the door."
    "Ah.. there is a person inside."

    scene bg classroom with dissolve
    show Kirino Happy at slightright
    Kirino "President! We're here!"

    "Seems like that person is the club president."
    "She was drinking her tea while looking outside through the window."
    "When she heard Kirino's voice, she then looks at our direction."

    show Sara Surprised at centerright
    "??? " "Ah, Kirino!"
    show Sara Neutral 
    show Kotoha Neutral at slightleft

    "??? " "And.. who would that person be?"

    Kirino "She is Kotoha. She plays mahjong."

    Kotoha "My name is Kotoha."

    Kirino "I invited Kotoha here to play mahjong."

    "??? " "Kirino, I thought you know about our situation right now."
    "??? " "We don't have enough members to play Mahjong."

    Kirino "But I remember we can do a 3-player Mahjong."

    "??? " "Hmm.. I see.."

    Kirino "Ah, sorry for the late introduction."

    Kirino "Kotoha, She is the president of the Mahjong Club — Sara."

    show Sara Happy

    Sara "I'm Sara."
    Sara "So, are we doing 3-player Mahjong?"

    Kirino "Yes!"

    Sara "Alright then, let's set it u—"

    show Kotoha Surprised
    show Kirino Surprised
    show Sara Surprised

    "??? " "WAIT!"

    "Suddenly, another person slams open a door, and stops us."

    Sara "Hmm??"

    show Miko Happy at centerleft
    show Kirino Happy
    show Kotoha Neutral

    "??? " "I've heard everything!"
    "??? " "And you shall all be grateful!"

    Miko "Because I, Miko, shall be the fourth player!"

    Sara "Oh my, another one poppep up"

    show Sara Happy

    Sara "This might be interesting..."
    Sara "Alright then, join us Miko."

    show Kirino Surprised

    Kirino "Ehh-- are we really playing with her?"

    Sara "The more the merrier, right Kotoha?"

    show Kirino Happy

    "I don't care much, I just want to finish quickly."

    show Kotoha Neutral
    Kotoha "Sure..."

    show Kirino Neutral

    Kirino "Ehh~ fine.."

    show Miko Happy
    show Kirino Happy

    Miko "hmph hmph.. I will show you all how strong I am!"

    Sara "Alright everyone, let's start setting up the game."
    Sara "To make it short, let's not do a repeated dealer."

    "Everyone Nods"
    "We shuffled through the Mahjong tiles, before eventually setting everything up."

    # Show round status and tile hand
    screen round_status_1():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "East 1, Kotoha : Dealer"
                text "Dora Indicator : 6z"

    show screen round_status_1
    
    image hand v1 = Composite(
    (0.5 ,0.5),
    (0, 0), "5m",
    (150, 0), "5m",
    (300, 0), "7m",
    (450, 0), "0p",
    (600, 0), "0p",
    (750, 0), "6p",
    (900, 0), "7p",
    (1050, 0), "8p",
    (1200, 0), "9p",
    (1350, 0), "2s",
    (1500, 0), "9s",
    (1650, 0), "4z",
    (1800, 0), "6z",
    )
    show hand v1 at tile_transform

    "My hand looks solid for a starting hand."
    "I think I can just aim for Tanyao (All Simple)."
    "Especially with 2 red doras with me."

    # Hide the tile hand and info display after this part
    hide hand v1
    hide screen round_status_1

    screen round_status_2():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "East 1, Turn 2, Kotoha's turn"

    show screen round_status_2

    image hand v2 = Composite(
    (0.5 ,0.5),
    (0, 0), "1m",
    (150, 0), "2m",
    (300, 0), "5m",
    (450, 0), "5m",
    (600, 0), "7m",
    (750, 0), "0p",
    (900, 0), "0p",
    (1050, 0), "6p",
    (1200, 0), "7p",
    (1350, 0), "8p",
    (1500, 0), "9p",
    (1650, 0), "2s",
    (1800, 0), "9s",
    )
    show hand v2 at tile_transform

    "My hand is moving pretty well"
    "Oh, I got a 3 Circle."
    "Let's throw a 9 Bamboo."
    hide screen round_status_2

    hide hand

    Miko "Pon!"
    "Eh? Open triplet on a terminal tiles?"
    "What is this girl planning?"

    screen round_status_3():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "East 1, Turn 3, Kotoha's turn"

    show screen round_status_3


    image hand v3 = Composite(
        (0.5 ,0.5),
        (0, 0), "1m",
        (150, 0), "2m",
        (300, 0), "5m",
        (450, 0), "5m",
        (600, 0), "7m",
        (750, 0), "3p",
        (900, 0), "0p",
        (1050, 0), "0p",
        (1200, 0), "6p",
        (1350, 0), "7p",
        (1500, 0), "8p",
        (1650, 0), "9p",
        (1800, 0), "2s",
        )
    show hand v3 at tile_transform
    "a 6 Character.."
    hide screen round_status_3
    "Let's throw 2 Bamboo."
    
    hide hand

    Miko "Pon!"
    "I see, so she is planning to go for Toitoi (All Triplets)."

    image hand v4 = Composite(
            (0.5 ,0.5),
            (0, 0), "2m",
            (150, 0), "2m",
            (300, 0), "5m",
            (450, 0), "6m",
            (600, 0), "7m",
            (750, 0), "2p",
            (900, 0), "3p",
            (1050, 0), "0p",
            (1200, 0), "0p",
            (1350, 0), "5p",
            (1500, 0), "6p",
            (1650, 0), "7p",
            (1800, 0), "8p",
            (1950, 0), "9p"
            )
    show hand v4 at tile_transform

    "My hand is ready now."
    hide hand v4

    "All I need is wait for either 1 Circle, or 4 Circle."
    "Miko has gotten 3 open triplets."
    "And it's not the same suit."
    "So she really is aiming for Toitoi (All Triplets)."
    "For Kirino, her discards look weird."
    "As for the president.."
    "I still don't get her."
    "She haven't started her move yet."
    "Very suspicious."
    "I can only see 1 discards for both 1 Circle and 4 Circle."
    "I might still have a chance."
    "For now, let's just call a riichi."
    Kotoha "Riichi!"

    screen round_status_3():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "East 1, Turn 13, Miko's turn"

    show screen round_status_3



    "Seems like president is playing defensive right now."
    "For Miko.."
    "*Miko discards 2 Circle*"
    "Doesn't seem like it.."
    "Or is she?"
    hide screen round_status_3
    "Can't really judge her for now."
    "*Draws a 7 Character*"

    show Kotoha Sad

    "Still a miss."
    "*Discards 7 Character*"

    show Kotoha Neutral

    "Let's see what the president will discard."
    "*Sara discards 9 Circle*"
    "As for Kirino, I don't really expect much from her."
    Kirino  "Oh finally!"
    Kirino "Riichi!"
    "Kirino discards 8 Circle, and declares Riichi."

    show Kotoha Surprised

    "Eh? Riichi at this timing?"

    show Kotoha Sad

    "But considering that she is a beginner."

    show Kotoha Neutral

    "I don't think she knows my wait."

    show Kotoha Happy

    "Let's see it in the end."
    screen round_status_4():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "East 1, Turn 15, Kirino's turn"

    show screen round_status_4

    show Kotoha Neutral
    show Kirino Neutral

    Kirino  "ahh.. still not it."
    "*Kirino discards 4 Circle*"

    show Kotoha Happy

    "Finally it's here."
    hide screen round_status_4
    Kotoha  "Ron!"

    show Kirino Surprised

    Kirino "Ehh"

    show Miko Surprised
    show Sara Surprised

    Kotoha "Riichi, Tanyao (All Simple), Red Dora 2."
    Kotoha  "12000 points."
    Kirino  "Ehh that's too much!"

    show Miko Sad
    show Kirino Neutral

    Miko  "Ahh.. just a little more!"

    show Sara Neutral

    "*Kirino gives Kotoha 8000 points."
    "That should do for now.."
    "I hope nothing bad will happen to me after this."

    show Sara Sad

    Sara "Ahh~ too bad."

    screen round_status_4():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "East 2, Dealer : Miko"
                text "Dora Indicator : 2s"

    show screen round_status_4
    
    image hand v5 = Composite(
            (0.5 ,0.5),
            (0, 0), "2m",
            (150, 0), "3m",
            (300, 0), "6m",
            (450, 0), "9m",
            (600, 0), "2p",
            (750, 0), "3p",
            (900, 0), "3p",
            (1050, 0), "6p",
            (1200, 0), "1s",
            (1350, 0), "3s",
            (1500, 0), "7s",
            (1650, 0), "7s",
            (1800, 0), "1z",
            )
    show hand v5 at tile_transform
    show Kotoha Neutral
    show Sara Neutral
    show Kirino Happy
    show Miko Happy

    "Another nice starting hand."
    "I think I can try aiming for Sanshoku Doujun (Mixed Triple Sequence)"
    hide screen round_status_4
    hide hand v5
    screen round_status_5():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "East 2, Turn 4, Kotoha's turn"

    show screen round_status_5
    
    image hand v6 = Composite(
            (0.5 ,0.5),
            (0, 0), "1m",
            (150, 0), "2m",
            (300, 0), "3m",
            (450, 0), "6m",
            (600, 0), "2p",
            (750, 0), "3p",
            (900, 0), "3p",
            (1050, 0), "6p",
            (1200, 0), "6p",
            (1350, 0), "1s",
            (1500, 0), "2s",
            (1650, 0), "6s",
            (1800, 0), "7s",
            )
    show hand v6 at tile_transform
    "My hand is slowly forming."
    hide hand v6

    "*Draws a Red Dragon*"
    "I don't need this."
    "*Discards Red Dragon*"
    hide screen round_status_5
    Miko  "I'll take that red."
    Miko  "Pon!"

    show Kotoha Sad

    "Now she got 1 yaku (Pattern) from that."
    "I need to be wary of her from now on."

    screen round_status_6():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "East 2, Turn 10, Kotoha's turn"

    show screen round_status_6
    
    image hand v7 = Composite(
            (0.5 ,0.5),
            (0, 0), "1m",
            (150, 0), "2m",
            (300, 0), "3m",
            (450, 0), "2p",
            (600, 0), "3p",
            (750, 0), "3p",
            (900, 0), "6p",
            (1050, 0), "6p",
            (1200, 0), "1s",
            (1350, 0), "3s",
            (1500, 0), "6s",
            (1650, 0), "7s",
            (1800, 0), "8s",
            )
    show hand v7 at tile_transform
    show Kotoha Happy

    "It's getting closer.."
    hide hand v7
    hide screen round_status_6
    "*Draws a 3 Character*"

    show Kotoha Neutral

    "Hmm.. I don't need this.."
    "*Discards 3 Character*"

    show Kirino Surprised

    Kirino "Ahh- Pon!"

    show Kirino Happy

    "Oh, she called for that."
    "*Kirino discards 1 Chararcter*"
    "*Sara draws a tile*"

    show Sara Happy

    "I still don't understant what the president is thinking."
    "I can't sense her movement."
    "Yet she is smiling."
    "Like she is enjoying the game."
    "*Sara discards 9 Circle*"

    show Kirino Surprised

    Kirino "Pon!"

    show Kirino Happy

    "Is Kirino doing a Toitoi (All Triplet)..?"

    show Kotoha Sad

    "Doesn't matter. I need to keep wary of her as well just in case."
    screen round_status_7():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "East 2, Turn 13, Kotoha's turn"

    show screen round_status_7

    "*Draws a 1 Circle*"

    show Kotoha Happy

    "finally 1 Circle came to me."
    "Now.. All I need to do is to call riichi and discard 3 Circle."
    "3 Circle.. Is not a dora."
    "And 2 of this 3 Circle is already discarded."
    "And since both Kirino and Miko have already discarded 3 Circle."
    "It should be a safe tile."
    hide screen round_status_7
    Kotoha  "Riichi!"
    "*Discards 3 Circle*"
    "I hope this works."
    Sara  "Sorry Kotoha, but your Riichi will not pass."

    show Kotoha Surprised

    Kotoha  "What?"
    Sara  "Ron."
    image hand v81 = Composite(
            (0.5 ,0.5),
            (0, 0), "6m",
            (150, 0), "7m",
            (300, 0), "8m",
            (450, 0), "4p",
            (600, 0), "5p",
            (750, 0), "6p",
            (900, 0), "7p",
            (1050, 0), "8p",
            (1200, 0), "8p",
            (1350, 0), "8p",
            (1500, 0), "2s",
            (1650, 0), "3s",
            (1800, 0), "4s",
            )
    show hand v81 at tile_transform
    show Kotoha Sad

    Sara  "Pinfu (All Sequence), Tanyao (All Simple), Dora 1"

    show Miko Surprised
    show Kirino Surprised

    Sara  "3900 Points."
    hide hand v8
    "She purposely didn't declare Riichi to let my guard down."
    "I was too focused on Miko and Kirino with their open hands."
    "*Kotoha gives Sara 3900 Points*"

    show Kirino Sad
    show Miko Sad

    Sara  "Thank you~"

    show Kotoha Neutral

    "The president is scarily good."
    "Or is it just a coincidence?"

    show Kotoha Sad

    "Next time I won't let my guard down!"

    screen round_status_8():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "East 3, Kirino Dealer"
                text "Dora Indicator : 6p"

    show screen round_status_8
    
    image hand v8 = Composite(
            (0.5 ,0.5),
            (0, 0), "2m",
            (150, 0), "5m",
            (300, 0), "6m",
            (450, 0), "9m",
            (600, 0), "9m",
            (750, 0), "2p",
            (900, 0), "6p",
            (1050, 0), "8p",
            (1200, 0), "3s",
            (1350, 0), "9s",
            (1500, 0), "3z",
            (1650, 0), "5z",
            (1800, 0), "5z",
            )
    show hand v8 at tile_transform
    show Kirino Happy
    show Miko Happy

    "This might end up cheap."

    show Kotoha Neutral

    "Let's see what I can do with this starting hand."
    hide screen round_status_8
    hide hand v8
    "I just need to remember to stay on guard."

    screen round_status_9():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "East 3, Turn 1, Kotoha's turn"
    show screen round_status_9
    

    "Draws a 7 Circle"

    show Kotoha Happy

    "Oh, I got a dora tile."
    "Let's discard West tile."
    "Discards West Wind"
    hide screen round_status_9
    Miko "Kan!"

    show Kotoha Surprised

    Kotoha  "Eh? A Kan this early?"

    show Kotoha Neutral

    Miko "You'll see. *smirk*"
    "Not only did she Kan."
    "It's an open Kan."

    show Kotoha Sad

    "She could have gotten higher scores if she keeps it closed triplets."

    show Kotoha Neutral

    "What is she thinking?"
    "I hope it's nothing big."


    screen round_status_10():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "East 3, Turn 5, Kotoha's turn"
                text "New dora indicator : 6p1m"

    show screen round_status_10

    image hand v9 = Composite(
            (0.5 ,0.5),
            (0, 0), "1m",
            (150, 0), "2m",
            (300, 0), "5m",
            (450, 0), "6m",
            (600, 0), "9m",
            (750, 0), "9p",
            (900, 0), "2p",
            (1050, 0), "6p",
            (1200, 0), "7p",
            (1350, 0), "8p",
            (1500, 0), "5z",
            (1650, 0), "5z",
            (1800, 0), "5z",
            )
    show hand v9 at tile_transform
    show Kotoha Happy

    "Hmm.. My hand is almost done."
    hide hand v9
    hide screen round_status_10
    "*draws 3 Character*"
    "Oh, here comes the final tile."
    "I just need to declare Riichi and discard 2 Circle."
    Kotoha  "Riichi!"
    "*Kotoha declares Riichi, and discards 2 Circle*"
    Miko  "Pon!"

    show Kotoha Neutral

    "I knew she would aim for another Toitoi (Open Triplets)."
    "*Miko discards 4 Bamboo*"
    "It's my turn again."
    "*Draws 8 Bamboo*"

    show Kotoha Sad

    "Ah.. not what i wanted."
    "*Discards 8 Bamboo*"

    show Kotoha Surprised
    show Sara Surprised
    show Kirino Surprised

    Miko "Ron!"
    image hand v10 = Composite(
            (0.5 ,0.5),
            (0, 0), "2m",
            (150, 0), "2m",
            (300, 0), "7p",
            (450, 0), "7p",
            (600, 0), "7p",
            (750, 0), "6s",
            (900, 0), "7s",
            (1050, 0), "2p",
            (1200, 0), "2p",
            (1350, 0), "2p",
            (1500, 0), "3z",
            (1650, 0), "3z",
            (1800, 0), "3z",
            (1950, 0), "3z",
            )
    show hand v10 at tile_transform
    Kotoha  "!?"

    show Kirino Neutral
    show Sara Neutral

    Miko  "Wind Tile, Dora 5."
    Miko  "12000 Points" 

    show Kirino Happy
    show Sara Happy

    Kirino "12000!? That's a lot!"

    show Kotoha Sad

    Kotoha "ugh.."
    "*Kotoha gives Miko 12000 Points*"
    Miko  "Let's go!"
    Miko  "My first win!"
    hide hand v10
    "I guess my feeling is just not there yet."
    "*Sara stares at Kotoha*"

    show Kotoha Surprised

    Kotoha  "Hmm? What's the matter President?"

    show Kotoha Neutral

    Sara  "Oh, it's nothing."

    screen round_status_11():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "East 4, Dealer : Sara"
                text "Dora Indicator : 5z"

    show screen round_status_11
    image hand v11 = Composite(
            (0.5 ,0.5),
            (0, 0), "2m",
            (150, 0), "5m",
            (300, 0), "6m",
            (450, 0), "1p",
            (600, 0), "3p",
            (750, 0), "5p",
            (900, 0), "9p",
            (1050, 0), "9s",
            (1200, 0), "1z",
            (1350, 0), "2z",
            (1500, 0), "4z",
            (1650, 0), "4z",
            (1800, 0), "6z",
            )
    show hand v11 at tile_transform
    show Kotoha Surprised

    "Ehh.. What kind of hand is this."

    show Kotoha Happy

    "If I'm lucky enough, I might be able to do Kokushi Musou (13 Orphans; Yakuman)"
    hide hand v11
    hide screen round_status_11

    show Kotoha Neutral

    "But.. I'm not going to play such high risk hand."

    screen round_status_12():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "East 4, Turn 1, Kotoha's turn"
                text "Dora Indicator : 5z"

    show screen round_status_12
    

    "*Draws 1 Character*"
    "I guess this works."
    "Lets clean the Honor tiles first."
    "*Discards Green Dragon*"
    hide screen round_status_12

    screen round_status_12():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "East 4, Turn 3, Kotoha's turn"

    show screen round_status_12
    image hand v12 = Composite(
            (0.5 ,0.5),
            (0, 0), "1m",
            (150, 0), "2m",
            (300, 0), "5m",
            (450, 0), "6m",
            (600, 0), "1p",
            (750, 0), "2p",
            (900, 0), "3p",
            (1050, 0), "5p",
            (1200, 0), "9p",
            (1350, 0), "9s",
            (1500, 0), "2z",
            (1650, 0), "4z",
            (1800, 0), "4z",
            )
    show hand v12 at tile_transform

    "So far, I see no movements from everyone."
    "*Draws 8 Bamboo*"
    hide screen round_status_12
    "This counts as a progress."
    "If I can just achieve a ready hand, everything should be fine."

    hide hand

    "*Discards North Wind*"

    screen round_status_13():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "East 4, Turn 7, Kotoha's turn"

    show screen round_status_13
    image hand v13 = Composite(
            (0.5 ,0.5),
            (0, 0), "1m",
            (150, 0), "2m",
            (300, 0), "3m",
            (450, 0), "5m",
            (600, 0), "6m",
            (750, 0), "1p",
            (900, 0), "2p",
            (1050, 0), "3p",
            (1200, 0), "5s",
            (1350, 0), "6s",
            (1500, 0), "8s",
            (1650, 0), "8s",
            (1800, 0), "9s",
            )
    show hand v13 at tile_transform
    show Kotoha Happy

    "Alright, it's shaping beautifully."
    "I just need 7 Bamboo, and I can declare my Riichi."
    "*Draws Red Dragon*"

    show Kotoha Sad
    hide hand

    "Ahh.. A miss.."
    "*Discards Red Dragon*"
    hide screen round_status_13
    screen round_status_14():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "East 4, Turn 8, Kirino's turn"

    show screen round_status_14

    show Kotoha Neutral

    "*Kirino draws a tile*"
    Kirino  "Alright! Riichi!"
    "*Kirino declares Riichi, and discards 5 circle*"
    hide screen round_status_14

    show Kotoha Surprised

    "That was quite fast."

    show Kotoha Neutral

    "*Sara draws a tile*"
    "*Sara discarded 4 Circle*"
    "*Draws Red Dragon*"
    "Hmm.."
    "I've discarded 1 Red Dragon, and Miko also had discarded 1 Red Dragon before."
    "There is only 2 Red Dragons left."
    "I don't think anyone would do a 1 tile wait."
    "*Discards Red Dragon*"

    show Kotoha Surprised

    Kirino  "YES! RON!"
    image hand v13 = Composite(
            (0.5 ,0.5),
            (0, 0), "4p",
            (150, 0), "5p",
            (300, 0), "6p",
            (450, 0), "8p",
            (600, 0), "8p",
            (750, 0), "8p",
            (900, 0), "2s",
            (1050, 0), "3s",
            (1200, 0), "4s",
            (1350, 0), "6s",
            (1500, 0), "7s",
            (1650, 0), "8s",
            (1800, 0), "7z",
            )
    show hand v13 at tile_transform
    show Sara Surprised
    show Miko Surprised

    Kotoha  "!?"
    Kirino  "Riichi Ippatsu! And.. That's it I think."

    show Sara Happy
    show Miko Neutral

    Sara  "Kirino, don't forget to check for Ura Dora."

    show Kotoha Sad

    Kirino  "Ah yes, Ura Dora."
    "*Kirino flips the Ura Dora*"
    screen round_status_15():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "Ura Dora Indicator : 1s"

    show screen round_status_15
    
    Kirino  "Yes! Ura Dora 1!"
    hide screen round_status_15
    hide hand v13
    Kirino  "Total Points are.."
    "*Kirino starts calculating the points*"

    show Kirino Neutral

    Kirino  "3900..? Wait no.."

    show Kirino Happy

    Kirino  "5200 Points!"
    Sara  "That is correct, Kirino!"
    Kirino  "Alright!"

    show Miko Surprised

    Miko  "How can a beginner like her is playing Mahjong with us right now!"

    show Miko Neutral

    Sara  "Calm down, calm down Miko."
    Sara  "She is still a beginner after all."

    show Miko Sad

    Sara  "Besides, we are just playing it for fun right?"
    Sara  "This will also be a good experience for Kirino herself."

    show Miko Neutral

    Miko  "Tch.. Fine.."
    "What a weird person."
    "*Kotoha gives Kirino 5200 Points*"
    Kirino  "Yay! My first win!"

    screen round_status_16():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "South 1, Dealer : Kotoha"
                text "Dora Indicator : 7s"

    show screen round_status_16

    
    image hand v14 = Composite(
            (0.5 ,0.5),
            (0, 0), "3m",
            (150, 0), "0p",
            (300, 0), "6p",
            (450, 0), "8p",
            (600, 0), "8p",
            (750, 0), "9p",
            (900, 0), "9p",
            (1050, 0), "1s",
            (1200, 0), "2s",
            (1350, 0), "4s",
            (1500, 0), "9s",
            (1650, 0), "1z",
            (1800, 0), "5z",
            )
    show hand v14 at tile_transform
    show Kotoha Neutral

    "*Draws South Wind*"
    hide screen round_status_16
    screen round_status_17():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "South 1, Turn 1, Kotoha's turn"

    show screen round_status_17

    show Kotoha Sad

    "I don't like this.."
    "I've been ron'd 3 times in a row."
    "*Discards South Wind*"
    hide screen round_status_17

    screen round_status_18():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "South 1, Turn 2, Kotoha's turn"

    show screen round_status_18



    image hand v15 = Composite(
            (0.5 ,0.5),
            (0, 0), "3m",
            (150, 0), "0p",
            (300, 0), "6p",
            (450, 0), "8p",
            (600, 0), "8p",
            (750, 0), "9p",
            (900, 0), "9p",
            (1050, 0), "1s",
            (1200, 0), "2s",
            (1350, 0), "4s",
            (1500, 0), "9s",
            (1650, 0), "1z",
            (1800, 0), "5z",
            )
    show hand v15 at tile_transform

    "*Draws 6 Circle*"
    "At this point, I might lose."
    "No.. This is for the best."
    "*Discards East Wind*"
    hide screen round_status_18

    show Miko Happy

    Miko  "Pon!"
    "*Miko discards Green Dragon*"
    "I knew she would go for it again."

    screen round_status_19():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "South 1, Turn 6, Kotoha's turn"

    show screen round_status_19
    
    image hand v16 = Composite(
            (0.5 ,0.5),
            (0, 0), "3m",
            (150, 0), "7m",
            (300, 0), "0p",
            (450, 0), "6p",
            (600, 0), "6p",
            (750, 0), "7p",
            (900, 0), "8p",
            (1050, 0), "8p",
            (1200, 0), "9p",
            (1350, 0), "9p",
            (1500, 0), "1s",
            (1650, 0), "2s",
            (1800, 0), "4s",
            )
    show hand v16 at tile_transform
    show Kotoha Neutral

    "*Draws 6s Character*"
    "My family would have hated it if I kept on winning."
    "*Discards 4 Bamboo*"
    hide screen round_status_19
    Miko  "Pon!"
    "So It's better if I just play casually."

    screen round_status_20():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "South 1, Turn 9, Kirino's turn"

    show screen round_status_20

    

    "*Kirino draws a tile*"
    "*Kirino discards 9 Character*"
    hide screen round_status_20
    Miko  "Kan!"
    "*Miko discards White Dragon*"
    screen round_status_21():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "New dora indicator : 7s7p"

    show screen round_status_21

    show Kotoha Sad

    "No matter who wins, everyone will be happy as long as I didn't win."
    hide screen round_status_21
    "*Kirino draws a tile*"
    "*Kirino discards 4 Circle*"
    "*Sara draws a tile*"
    Sara  "You know Kotoha.."
    Sara  "I don't know what happened in your past."
    Sara  "But remember this."
    Sara  "The more you hold back, the less fun we have."
    Sara  "That's why Kotoha.."
    Sara  "Bring out your all!"
    Sara  "Riichi!"
    "*Sara declares Riichi, and discards 5 Circle*"

    show Kotoha Neutral

    "..."
    "What President Sara said is right.."
    "I'm not playing with my family right now."

    show Kotoha Happy

    "So It's fine if I try to do better."
    "..."
    Kotoha  "Hehe.. *Smiles*"
    Kotoha "Challenge accepted president!"
    image hand v16 = Composite(
            (0.5 ,0.5),
            (0, 0), "3m",
            (150, 0), "7m",
            (300, 0), "0p",
            (450, 0), "6p",
            (600, 0), "6p",
            (750, 0), "6p",
            (900, 0), "7p",
            (1050, 0), "8p",
            (1200, 0), "8p",
            (1350, 0), "8p",
            (1500, 0), "9p",
            (1650, 0), "9p",
            (1800, 0), "2s",
            )
    show hand v16 at tile_transform
    "*Draws 5 Circle*"
    "Hmm.. 2 Bamboo is not really a safe discard."
    "No.. I will trust in my instinct.."
    "*Discards 2 Bamboo*"

    show Miko Sad

    Miko  "*In Mind* This girl.. her smile just now is scary.."
    Miko  "*In Mind* And she has not played seriously this whole time??"
    Miko  "*In Mind* Don't joke with me!"
    Miko  "*In Mind* I will prove to everyone that I am the best!"

    screen round_status_22():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "South 1, Turn 11, Kotoha's turn"

    show screen round_status_22

    image hand v17 = Composite(
            (0.5 ,0.5),
            (0, 0), "7m",
            (150, 0), "7m",
            (300, 0), "0p",
            (450, 0), "5p",
            (600, 0), "6p",
            (750, 0), "6p",
            (900, 0), "6p",
            (1050, 0), "7p",
            (1200, 0), "8p",
            (1350, 0), "8p",
            (1500, 0), "8p",
            (1650, 0), "9p",
            (1800, 0), "9p",
            )
    show Miko Neutral
    show hand v17 at tile_transform
    "*Draws 6 Character*"
    "Oh.. 6 Character.."
    "I am pretty close to Suuanko (Four Concealed Triplet; Yakuman)"
    "But I feel like this is a trap."
    hide screen round_status_22
    hide hand v17
    "Just to be safe, I will discard 6 Circle."
    "*Discard 6 Circle*"
    "I know it's a little bit weird, but I know this is the correct answer."

    screen round_status_23():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "** South 1, Final Turn, Kotoha's turn **"

    show screen round_status_23

    
    image hand v17 = Composite(
            (0.5 ,0.5),
            (0, 0), "6m",
            (150, 0), "7m",
            (300, 0), "7m",
            (450, 0), "0p",
            (600, 0), "5p",
            (750, 0), "6p",
            (900, 0), "6p",
            (1050, 0), "7p",
            (1200, 0), "8p",
            (1350, 0), "8p",
            (1500, 0), "8p",
            (1650, 0), "9p",
            (1800, 0), "9p",
            )
    show hand v17 at tile_transform

    "*Draws 5 Character*"
    "Ok.. 7 Character is safe to throw now."
    "I saw Sara discarded that tile a few rounds ago."
    "*Discards 7 Character*"
    hide screen round_status_23
    screen round_status_24():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "South 1, Final Turn, Sara's turn"

    show screen round_status_24
    

    "*Sara draws a tile*"
    "*Sara discards 4 Circle*"
    hide screen round_status_24

    show Kirino Sad

    Kirino  "Not tenpai.. (No Ready Hand)"
    Sara  "Tenpai (Ready Hand)."
    Kotoha  "Tenpai (Ready Hand)."

    show Miko Happy

    Miko  "Tenpai (Ready Hand)."

    show Kirino Surprised

    Kirino  "Ahh---! I'm the only one with Not Tenpai (Not Ready Hand)!"

    show Kirino Sad

    Sara  "*In Mind* Ahh.. I knew she can do it."

    show Sara Sad

    Sara  "Ahh~ too bad.."

    show Kotoha Neutral

    "I survived.."
    "I managed to defend myself this time.."

    show Sara Happy
    show Kirino Happy

    "*Kirino gives 1000 points to everyone*"

    screen round_status_25():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "South 2, Dealer : Miko"
                text "Dora Indicator : 7z"

    show screen round_status_25
    
    image hand v18 = Composite(
            (0.5 ,0.5),
            (0, 0), "3m",
            (150, 0), "5m",
            (300, 0), "5m",
            (450, 0), "9m",
            (600, 0), "3p",
            (750, 0), "7p",
            (900, 0), "8p",
            (1050, 0), "2s",
            (1200, 0), "4s",
            (1350, 0), "6s",
            (1500, 0), "2z",
            (1650, 0), "5z",
            (1800, 0), "5z",
            )
    show hand v18 at tile_transform

    "Oh, 2 dora is in my hand."
    "Alright.. Lets do this."
    hide screen round_status_25

    screen round_status_26():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "South 2, Turn 1, Kotoha's turn"
                text "Dora Indicator : 7z"

    show screen round_status_26
    
    "*Draws South Wind*"

    show Kotoha Surprised

    "My, I got South."
    "I am in South direction, that's 1 Yaku (Pattern) for me."

    show Kotoha Happy

    "And since it's in South round, that's another Yaku (Pattern) for me." 
    "If everything goes well, 12000 Points is guaranteed for me."
    hide hand v18
    "*Discards 9 Character*"
    hide screen round_status_26
    "*Miko draws a tile*"
    "*Miko discards South Wind*"

    show Kotoha Surprised

    "Oh, it's out."

    show Kotoha Happy

    Kotoha  "Pon!"
    "*Discards 3 Circle*"
    Miko "I won't lose to you!"
    Miko  "Pon!"
    "*Discards North Tile*"
    "*Kirino draws a tile*"
    "*Kirino discards White Dragon*"

    show Kotoha Surprised

    "Oh,  got another one!"

    show Kotoha Happy

    Kotoha  "Pon!"
    "*Discards 3 Character*"

    show Kirino Surprised

    Kirino  "Kotoha, you are scary~!"

    show Kirino Sad

    Kirino  "Since when did you turn aggresive?"

    show Kirino Happy

    Kotoha  "Hahaha.. Only this time, Kirino."
    Sara  "haha.. My oh my.."

    screen round_status_27():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "South 2, Turn 4, Kotoha's turn"

    show screen round_status_27
    
    image hand v19 = Composite(
            (0.5 ,0.5),
            (0, 0), "5m",
            (150, 0), "5m",
            (300, 0), "7p",
            (450, 0), "8p",
            (600, 0), "2s",
            (750, 0), "3s",
            (900, 0), "4s",
            (1050, 0), "2z",
            (1200, 0), "2z",
            (1350, 0), "2z",
            (1500, 0), "5z",
            (1650, 0), "5z",
            (1800, 0), "5z",
            )
    show hand v19 at tile_transform
    "*Draws 5 Circle*"
    "Almost!"

    hide hand

    "*Discards 5 Circle*"
    hide screen round_status_27

    screen round_status_28():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "South 2, Turn 7, Sara's turn"
    show screen round_status_28


    "*Sara draws a tile*"
    Sara  "Hmm.. why not."
    Sara  "Kan."
    "*Sara Makes a closed quads of Green Dragon*"
    "*Sara draws a tile*"
    hide screen round_status_28

    screen round_status_29():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "New Dora Indicator : 2s"
    show screen round_status_29


    "*Sara discards 4 Character*"

    "Nice, new dora!"
    hide screen round_status_29

    image hand v19 = Composite(
            (0.5 ,0.5),
            (0, 0), "5m",
            (150, 0), "5m",
            (300, 0), "7p",
            (450, 0), "8p",
            (600, 0), "2s",
            (750, 0), "3s",
            (900, 0), "4s",
            (1050, 0), "2z",
            (1200, 0), "2z",
            (1350, 0), "2z",
            (1500, 0), "5z",
            (1650, 0), "5z",
            (1800, 0), "5z",
            )
    show hand v19 at tile_transform
    "*Draws West Wind*"

    show Kotoha Sad

    "Ahh.. still not here yet.."

    show Kotoha Neutral

    "*Discards West Wind*"

    "*Miko draws a tile*"
    "*Miko discards 6 Circle*"

    show Kotoha Happy
    show Miko Surprised
    show Kirino Surprised

    Kotoha  "Ron!"
    Miko  "Wha-!?"

    show Kirino Sad

    Kotoha  "Wind Tile, Round Wind Tile, Dragon Tile, Dora 3."
    Kotoha "12000 Points."
    Sara  "Ooh~ another big one."

    show Kirino Happy

    Kirino  "That's amazing!"

    screen round_status_30():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "South 3, Dealer : Kirino"
                text "Dora Indicator : 7p"
    show screen round_status_30
    

    image hand v20 = Composite(
            (0.5 ,0.5),
            (0, 0), "2m",
            (150, 0), "2m",
            (300, 0), "0m",
            (450, 0), "6m",
            (600, 0), "7m",
            (750, 0), "8m",
            (900, 0), "3p",
            (1050, 0), "0p",
            (1200, 0), "1s",
            (1350, 0), "4s",
            (1500, 0), "5s",
            (1650, 0), "2z",
            (1800, 0), "7z",
            )
    show hand v20 at tile_transform
    show Miko Sad

    "*Draws 4 Bamboo*"
    hide screen round_status_30
    screen round_status_31():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "South 3, Turn 1, Kotoha's turn"
    show screen round_status_31

    "Not a bad start."
    "*Discards South Wind*"
    hide screen round_status_31

    
    screen round_status_32():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "South 3, Turn 5, Kotoha's turn"
    show screen round_status_32

    image hand v20 = Composite(
            (0.5 ,0.5),
            (0, 0), "2m",
            (150, 0), "2m",
            (300, 0), "0m",
            (450, 0), "5m",
            (600, 0), "6m",
            (750, 0), "7m",
            (900, 0), "8m",
            (1050, 0), "3p",
            (1200, 0), "4p",
            (1350, 0), "0p",
            (1500, 0), "4s",
            (1650, 0), "4s",
            (1800, 0), "5s",
            )
    show hand v20 at tile_transform
    show Miko Neutral

    "*Draws 5 Character*"
    "Oh sweet!"
    hide screen round_status_32
    Kotoha  "Riichi!"
    "*Declares Riichi and discards 5 Bamboo*"

    show Miko Surprised

    Miko "That was fast!"

    show Miko Neutral

    Sara "Fufu.. Not bad, Kotoha."

    screen round_status_33():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "South 3, Turn 11, Kotoha's turn"
    show screen round_status_33
    

    "*Draws South Tile*"

    show Kotoha Sad

    "The tile is not coming out."
    hide screen round_status_33
    "Seems like everyone also decides to fold."
    screen round_status_33():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "South 3, Last Turn, Sara's turn"
    show screen round_status_33

    show Kotoha Neutral

    "*Sara draws a tile*"
    "*Sara discards 7 Circle*"
    image hand v211 = Composite(
            (0.5 ,0.5),
            (0, 0), "2m",
            (150, 0), "2m",
            (300, 0), "0m",
            (450, 0), "5m",
            (600, 0), "5m",
            (750, 0), "6m",
            (900, 0), "7m",
            (1050, 0), "8m",
            (1200, 0), "3p",
            (1350, 0), "4p",
            (1500, 0), "0p",
            (1650, 0), "4s",
            (1800, 0), "4s",
            )
    show hand v211 at tile_transform

    "This is the last tile"
    "Please be it!"
    "*Draws 2 Character*"

    show Kotoha Happy

    "Yes! Got it!"
    hide screen round_status_33
    Kotoha  "Tsumo!"
    Kotoha  "Riichi, Tsumo (Fully Concealed Hand), Haitei Raoyue (Win on last drawn tile), Tanyao (All Simple), Red Dora 2"
    Kotoha  "3000 points from non-dealer, 6000 Points from dealer"
    hide hand v21
    show Kirino Surprised

    Kirino  "Ehh? Dealer lost more points?"

    show Miko Sad

    Sara  "That is right Kirino."
    Sara  "But in exchange, Dealer earn more when they win."

    show Kirino Happy

    Kirino  "I understand now."
    Miko  "And on top of that, she won on Haitei (Win on last drawn tile)."
    Miko  "That needs a lot of luck for that to happen."

    show Miko Happy

    Sara  "Exactly."
    "*Miko and Sara gives 3000 points to Kotoha, while Kirino gives 6000 Points*"

    screen round_status_34():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "South 4, Dealer : Sara"
                text "Dora Indicator : 2m"
    show screen round_status_34
    image hand v21 = Composite(
            (0.5 ,0.5),
            (0, 0), "1m",
            (150, 0), "5m",
            (300, 0), "9m",
            (450, 0), "1p",
            (600, 0), "6p",
            (750, 0), "8p",
            (900, 0), "1s",
            (1050, 0), "6s",
            (1200, 0), "8s",
            (1350, 0), "9s",
            (1500, 0), "1z",
            (1650, 0), "4z",
            (1800, 0), "7z",
            )
    show hand v21 at tile_transform
    show Kotoha Sad

    "Oh my.. This hand is hopeless."
    "Lets see what i can do with this kind of starting hand."
    hide screen round_status_34

    screen round_status_35():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "South 4, Turn 7, Kotoha's turn"
    show screen round_status_35
    
    image hand v22 = Composite(
            (0.5 ,0.5),
            (0, 0), "4p",
            (150, 0), "6p",
            (300, 0), "6p",
            (450, 0), "8p",
            (600, 0), "1s",
            (750, 0), "2s",
            (900, 0), "5s",
            (1050, 0), "5s",
            (1200, 0), "6s",
            (1350, 0), "7s",
            (1500, 0), "8s",
            (1650, 0), "8s",
            (1800, 0), "9s",
            )
    show hand v22 at tile_transform
    show Kotoha Happy

    "*Draws 5 Red Circle*"
    "So far, my hand is shaping perfectly fine."
    "But what I'm scared right now is.."
    "The fact that I haven't seen any Character Tiles so far."
    "I hope that no one gets a full flush of Character Tiles."
    "*Discards 8 Circle*"
    hide screen round_status_35
    screen round_status_36():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "South 4, Turn 11, Kotoha's turn"
    show screen round_status_36
    
    image hand v23 = Composite(
            (0.5 ,0.5),
            (0, 0), "4p",
            (150, 0), "0p",
            (300, 0), "6p",
            (450, 0), "8p",
            (600, 0), "1s",
            (750, 0), "2s",
            (900, 0), "5s",
            (1050, 0), "5s",
            (1200, 0), "6s",
            (1350, 0), "7s",
            (1500, 0), "8s",
            (1650, 0), "8s",
            (1800, 0), "9s",
            )
    show hand v23 at tile_transform

    "*Draws 4 Bamboo*"
    "Hmm.. Can I aim for a straight?"
    "Lets try it then."

    hide hand

    "*Discards 5 Bamboo*"
    hide screen round_status_36
    Miko  "Chi!"
    "*Miko discards South Tile*"

    show Kotoha Surprised

    "Oh, Miko made the first move."

    show Kotoha Sad

    "I don't like the look of this."

    screen round_status_37():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "South 4, Turn 13, Kotoha's turn"
    show screen round_status_37

    
    image hand v24 = Composite(
            (0.5 ,0.5),
            (0, 0), "4p",
            (150, 0), "0p",
            (300, 0), "6p",
            (450, 0), "1s",
            (600, 0), "2s",
            (750, 0), "4s",
            (900, 0), "5s",
            (1050, 0), "6s",
            (1200, 0), "7s",
            (1350, 0), "8s",
            (1500, 0), "8s",
            (1650, 0), "9s",
            (1800, 0), "9s",
            )
    show hand v24 at tile_transform
    show Kotoha Neutral

    "*Draws 3 Bamboo*"
    "Oh, Tenpai.. (Ready Hand)"

    show Kotoha Sad

    "But.. I don't like it.."
    "So far, I've seen no characters discarded"
    "For now, I'm not going to declare Riichi."
    "Time for me to observe the situation."
    "*Discard 8 Bamboo*"
    hide screen round_status_37
    screen round_status_38():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "South 4, Turn 14, Kotoha's turn"
    show screen round_status_38

    image hand v24 = Composite(
            (0.5 ,0.5),
            (0, 0), "4p",
            (150, 0), "0p",
            (300, 0), "6p",
            (450, 0), "1s",
            (600, 0), "2s",
            (750, 0), "4s",
            (900, 0), "5s",
            (1050, 0), "6s",
            (1200, 0), "7s",
            (1350, 0), "8s",
            (1500, 0), "8s",
            (1650, 0), "9s",
            (1800, 0), "9s",
            )
    show hand v24 at tile_transform
    show Kotoha Neutral

    "*Draws 6 Character*"
    "This late?"
    hide hand v24
    show Kotoha Sad

    "I don't trust it.."
    "I'm feeling suspicious of it.. I'm folding for now."
    "*Discards 5 Red Circle*"
    hide screen round_status_38
    Miko  "Pon!"
    "*Miko Discards 9 Bamboo*"
    "*Kirino draws a tile*"
    "*Kirino discards White Dragon*"
    "*Sara draws a tile*"

    show Kotoha Neutral

    Sara  "Ahh~.. Sorry girls, but I shall end our match right now."
    Sara  "Tsumo."

    image hand v25 = Composite(
            (0.5 ,0.5),
            (0, 0), "1m",
            (150, 0), "2m",
            (300, 0), "3m",
            (450, 0), "3m",
            (600, 0), "3m",
            (750, 0), "4m",
            (900, 0), "5m",
            (1050, 0), "7m",
            (1200, 0), "7m",
            (1350, 0), "8m",
            (1500, 0), "8m",
            (1650, 0), "9m",
            (1800, 0), "9m",
            (1950, 0), "6m",

            )
    show hand v25 at tile_transform
    show Kotoha Surprised
    show Kirino Surprised
    show Miko Surprised

    "I knew it!"
    Sara  "Tsumo (Fully Concealed Hand), Chinitsu (Full Flush), Ittsu (Straight), Iipeikou (Double Sequence), Pinfu (All Sequence), Dora 3."
    Sara "And since i'm the dealer, It's 48000—Yakuman!"
    Miko  "Yakuman? for real!?"
    Kirino  "That's so big!"
    Kotoha  "What a deadly silent hand.."
    Sara  "Ahaha.."

    show Kotoha Neutral
    show Kirino Happy
    show Miko Neutral

    Sara  "With this, our match comes to an end."
    hide hand v25

    screen round_status_39():
        frame:
            xalign 0.5 ypos 50
            vbox:
                spacing 10
                text "Final Score :"
                text "Sara : 74900"
                text "Kotoha : 30100"
                text "Miko : 8000"
                text "Kirino : -7800"


    show screen round_status_39

    show Miko Sad
    show Kotoha Happy

    Miko "Ahhh! I'm so frustrated right now!"
    Sara  "No need to feel frustrated Miko."
    hide screen round_status_39
    Sara  "It's all about having fun!"
    Kirino  "Yes! I had a lot of fun!"
    Kirino  "Miko, President Sara, and Kotoha are all amazing!"
    Kirino  "I wish that one day I could play like everyone!"
    Kotoha  "I'm not as amazing as you thought."

    show Miko Neutral

    Sara  "Don't say it like that, Kotoha."
    Sara "You are amazing."

    show Miko Happy

    Kotoha  "Thank you.. President Sara.."
    Kotoha  "Also, it is thanks to you that I had fun."
    Kotoha  "Once again, thank you!"
    Sara  "It's fine~ As long as you have fun, I'm happy about it."
    Sara  "So Kotoha.. After you know how to have fun again in Mahjong, do you want to join the club?"

    show Kotoha Surprised

    Kotoha  "Can I?"

    show Kotoha Happy

    Kirino "Of course! We are lacking members right now, so we would be happy!"
    "Maybe i should start playing Mahjong again."
    "Thanks to President Sara, I can start enjoying Mahjong again."
    Kotoha  "Alright.. I will join the club.. President!"

    show Sara Surprised

    Miko  "Hold on!"

    show Miko Happy
    show Sara Neutral

    Sara "Hmm?"
    Miko "I'm also joining the club!"

    show Sara Surprised

    Sara "Oh?"

    show Sara Happy

    Miko  "I'll join the club, then we can play again!"
    Miko  "One day I will become better than Kotoha, and You!"

    show Sara Surprised

    Sara  "wahh~ I don't like your motive, but you are also welcomed, Miko."

    show Sara Happy

    Miko  "Yes!"
    Sara  "Alright then. Since we've got 4 members now."
    Sara  "We can start our club activity tomorrow!"
    Kirino "Are we going to play again tomorrow?"
    Sara  "For sure!"
    Miko  "I won't lose to you guys again!"
    Kotoha  "Ahaha.. good luck with that."
    "This place might be the perfect place for me."
    "For the first time after a long time, I learned how to enjoy Mahjong again."
    "And everyone is very kind, and passionate about Mahjong."
    "Hehe.. Might as well enjoy it for as long as I can."

    "*TO BE CONTINUED*"


