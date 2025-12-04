# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define alex = Character("Alex", kind=adv, image="alex", what_font="fonts/Alex.ttf", who_font="fonts/Alex.ttf")
define journal = Character(None, kind=nvl, what_font="fonts/Alex.ttf")
define narration = Character(None, kind=adv, what_font="fonts/Alex.ttf", who_font="fonts/Alex.ttf")
define claudia = Character("Claudia", kind=adv, image="claudia", what_font="fonts/Claudia.ttf", who_font="fonts/Claudia.ttf")
define tsukune = Character("Tsukune", kind=adv, image="tsukune", what_font="fonts/Tsukune.ttf", who_font="fonts/Tsukune.ttf")
define rando = Character("???", kind=adv, image="alex", what_font="fonts/Alex.ttf", who_font="fonts/Alex.ttf")
define witness = Character("Witness", kind=adv, image="witness", what_font="fonts/Alex.ttf")


# The game starts here.

label start:
    stop music
    scene bg_alex_apartment_living_room with Dissolve(2.0)
    jump chapter_0_journal_1

label chapter_0_journal_1:
    journal "June 12, 2023 - Monday @ 7:05 AM"
    journal "I slept like usual, another nightmare. The thing is that I can't remember what the nightmare even was."
    journal "All I can recall is waking up feeling afraid with sweat all over me. It sucks to be woken up like that every morning. Hopefully the nightmares settle down one of these days..."
    play sound "sfx/thud_1.mp3"
    journal "Other than that, I'm really liking doing these journal entries. Sure, it's weird to feel like you're talking to a wall at first, but there's something therapeutic about it. It's like someone is letting you vent to them for as long as you're willing to keep writing with a pen."
    nvl clear
    journal "It's nice to feel listened to, even if it's just a little journal holding all my thoughts together."
    journal "There is something that I recently realized that I'm struggling with. I didn't realize that I was feeling lonely for as long as I have."
    journal "I thought I was just uncomfortable about being alone for too long at a time, but I'm also horrible at reaching out to people."
    play sound "sfx/muffled_noise_1.mp3"
    journal "I'd like to stay on top of talking with people, but it just ends up slipping my mind. I forget to talk to people until it's been so long that it'd feel out of place for me to reach out to them."
    nvl clear
    play sound "sfx/thud_1.mp3"
    journal "I also noticed that I'm starting to learn to identify my emotions better after journaling for the past month. I make it a point to ask myself, \"What am I feeling?\" when I write these entries because it's more than just venting about my problems."
    journal "If I know what I'm feeling, then it makes it easier to learn how to manage my emotions better. I guess re-learning emotions is common after suppressing them for so many years..."
    play sound "sfx/thud_1.mp3"
    show alex_thinking
    narration "It's usually never this noisy this early in the morning, especially since the unit next to me is empty. What's all the noise about?"
    play sound  "sfx/door_lock.mp3"
    jump chapter_0_meet_claudia

label chapter_0_meet_claudia:
    scene bg_apartment_outside with fade
    rando "Alright Claudia, you take care!"
    play sound  "sfx/carDoor_close.mp3"
    show claudia_neutral:
        xpos 240
        easein 0.5 xpos 0
    claudia "Thanks Toby, I appreciate your help!"
    play sound  "sfx/carDrive_start.mp3"
    alex "..."
    alex "O-oh, hey there!"
    narration "Smooth."
    claudia "Hi there, I didn't mean to startle you. I just moved my things in with my friend. Were we too loud?"
    alex "Well if you're moving in, don't worry about the noise. It's a one-time thing I'm sure. I guess you're my neighbor, right?"
    claudia "Yup! It took a couple hours to get everything out of the moving van, but I still have to unpack stuff. It'll be a while before everything is out of those boxes, but I'll try to keep the noise down!"
    claudia "Moving to a new place can be pretty challenging, but I needed the change of scenery."
    alex "It can be good to move to a new area. Fresh starts, you know?"
    claudia "I'm definitely with you there. My name's Claudia. What about you?"
    alex "Oh, I'm Alex. I don't have any nicknames, though. My name is kinda too short for that."
    alex "I'm kinda surprised it took them two and a half years to fill that unit."
    claudia "It's been that long? I better make sure to deep clean it then. I can't stand when dust builds up, and you know that maintenance doesn't do upkeep with empty units."
    alex "I get what you mean. It can be a struggle sometimes to pick up the slack for lazy apartment managers, right?"
    claudia "Heh... Yeah, it is."
    claudia "So... you've lived here for a while?"
    alex "Yeah, I've been here for about three years now."
    claudia "There aren't any roaches here, right?"
    alex "Oh, no! They have pest control come out here every week, so wer don't have any pests like that around here."
    claudia "That's great. The place before the one I just moved from had a pretty bad roach infestation. You can thank the hoarder neighbors for that."
    claudia "Anyways, I'd better start unpacking and cleaning. I'll see you later!"
    alex "See you later!"
    narration "I should probably start heading off. I might be cutting it kinda close..."
    scene bg_car_driver with fade
    narration "\"See you later?\" I didn't think I'd get along with someone new so easily! Hopefully that's a good sign."
    narration "I felt pretty awkward when talking to her though..."
    narration "It's good to know she's interested in seeing me again, at least."
    jump chapter_0_journal_2

label chapter_0_journal_2:
    scene black with fade
    narration "I didn't spend as much time as I wanted to on my journaling this morning."
    narration "Maybe if I spend a couple of minutes doing it now, no one will notice?"
    scene bg_work_desk with dissolve
    journal "8:02 AM"
    journal "I have something on my mind, or rather someone. I have a new neighbor that moved in to the unit right next to me."
    journal "Her name is Claudia and I was able to say hi to her right before I left for work. She and her friend were making a lot of noise when moving things inside the unit but as long as it doesn't keep happening, it's okay."
    journal "Something sticks out about her though... I just can't tell what it is exactly. It would be nice if we ended up becoming friends. I don't think friendships start that fast though, so maybe it'll take some time."
    jump chapter_0_meet_tsukune

label chapter_0_meet_tsukune:
    scene bg_office
    # play sound footsteps_1
    nvl clear
    narration "Oh shit, Tsukune's coming!"
    tsukune "Hey Alex, how's it going?"
    alex "I'm doing pretty good! I found out I have a new neighbor this morning."
    alex "You're pretty upbeat like usual. How's your morning?"
    tsukune "About that... I had to take the bus to get to work today."
    tsukune "Yesterday, my car's AC compressor seized up and snapped the serpentine belt, so now my car's in the shop until they get the parts delivered to replace what got trashed."
    alex "That sucks! How much did it cost to get here by bus?"
    tsukune "It was about $3.50 just to get here, but I could only use coins or cash. They don't do card on any of the buses in town apparently."
    tsukune "I'll live though! It could be a lot more expensive like in some other cities."
    tsukune "Anyways, I should probably get to my desk now. Don't wanna get in any trouble."
    alex "Wait, before you go, I can take you to and from work until your car is fixed. We live in the same apartment complex after all."
    tsukune "Really? Are you sure that's fine? I can pay you back in gas mon-"
    alex "Don't worry about it, it's on me. I wanna help you out if I can, and it's not like I'm going out of my way to take you home."
    alex "I'm still doing the same drive as usual, just with an extra person in the car with me."
    tsukune "You're a great friend, Alex. I'll meet you after work, alright?"
    narration "Tsukune's right, we should get back to work before we get in trouble. Let's go!"
    jump chapter_0_driving_home

label chapter_0_driving_home:
    scene black with fade
    alex "..."
    alex "Oh, it's time to clock out. I better not keep Tsukune waiting!"
    scene bg_car_passenger with fade
    tsukune "Thanks for driving me home. This is way more convenient than taking the bus."
    alex "That, and you know someone hasn't threw up where you're sitting?"
    tsukune "Wait, huh?"
    alex "O-oh, it's just- You know how sometimes people throw up in taxis when they get drunk?"
    alex "Well, I don't drive other people in my car, so everything is clean."
    tsukune "Ohhh, you're totally right. It'd suck to sit on someone's vomit stains."
    alex "See, you get me! This is why you're awesome."
    scene bg_car_driver with dissolve
    alex "Actually, I've been meaning to ask... How're you doing lately? Like, how are you actually doing?"
    tsukune "Oh... damn, it's been a while since someone's asked me that..."
    tsukune "But I'm doing pretty well. Actually, I think I've been doing a lot better lately."
    alex "What do you mean?"
    tsukune "Well... Geez, it's kind of embarassing to admit it, but I've started seeing a therapist again."
    alex "... Again?"
    tsukune "Yeah, I was getting close to relapsing on smoking cigarettes for the first time in two years."
    alex "I never knew you smoked."
    tsukune "Yeah, I don't really advertise it. It's not something I'm proud of being addicted to."
    alex "You're still addicted?"
    tsukune "You never really stop being addicted to things, I've learned."
    tsukune "Usually, it's either a person distracts themself from their addictions or they get themselves addicted to something that's better for you."
    tsukune "For me, I distract myself with creative activities. If I keep my hands busy, I'm less likely to think about smoking."
    scene bg_car_passenger
    alex "So how has therapy been helping you out?"
    tsukune "Having a professional to talk to about my issues helps to keep me more level-headed. It can be pretty easy for me to get into self-loathing loops."
    tsukune "The self-loathing is usually a trigger for my cigarette cravings."
    alex "I'm glad therapy is working is working out for you! I know it can be hard for people to start therapy."
    tsukune "It really can be, especially if you have an insurance that isn't commonly covered locally."
    tsukune "I'm just thankful that I quit smoking before I started working here. it sucks to have people side-eyeing you and talking shit for having an addiction."
    alex "Were your old coworkers mad about it?"
    tsukune "Mad isn't the right word... It was them being judgemental more than anything else."
    tsukune "They thought I couldn't hear them, but they made sure to change the topic real quick when I made my presence known."
    alex "Aw man, that really sucks... You're not dealing with that here, right?"
    tsukune "Luckily, I'm not dealing with that here."
    alex "Alright, we're pulling up."
    tsukune "Perfect timing!"
    scene bg_apartment_parking_lot with dissolve
    tsukune "Thanks again for dropping me off. I owe you for driving me!"
    alex "It's no problem, really."
    tsukune "Wait, did you want to go to the gym with me later?"
    alex "I would, but I wanna relax when I get home. I'm feeling pretty tired. Maybe next time?"
    tsukune "No big deal, I'll catch you later!"
    # play sound "car_driving.mp3"
    scene black with fade
    jump chapter_0_alex_return_home

label chapter_0_alex_return_home:
    scene bg_alex_apartment_living_room with fade
    # play sound "door_close.mp3"
    alex "Well, now that the day is over, I can spend some time relaxing."
    # play sound "thud.mp3"
    "*thud*"
    alex "... That Claudia girl must still be unpacking her boxes. Hopefully she's not working herself too hard."
    # play sound "rubbing(?).mp3"
    "*shff shff shff shff*"
    alex "Whatever she's doing, I hope she keeps the noise low once it gets later in the evening."
    alex "I should probably journal and then make something for me to eat."
    journal "4:17 PM"
    journal "Today went pretty well. I should probably write some things I'm grateful for today. I'm grateful that I got to work on time, I'm grateful that I met Claudia since she might become a new friend, and I'm grateful that I got to drive Tsukune home from work while his car is in the shop. I"
    return
