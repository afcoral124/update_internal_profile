#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from internal_profile_update.crew import InternalProfileUpdate

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


raw_updates="""

Juan & Molly  - January 22
VIEW RECORDING - 33 mins (No highlights): 

---

0:00 - Juan Vidri (Mvcvcapital)
  Hey, Cash, how are you?

0:01 - Ryan Cash (AcquiMatch)
  This meeting is being recorded. How about yourself?

0:06 - Juan Vidri (Mvcvcapital)
  I'm good, I'm good, and Molly's on her way, so she'll be here in a couple minutes, or in a minute.

0:13 - Ryan Cash (AcquiMatch)
  You all staying warm up there in Austin?

0:16 - Juan Vidri (Mvcvcapital)
  Yes, yes, we are. How about you?

0:19 - Ryan Cash (AcquiMatch)
  Yeah, just preparing for the end of the week, which is supposed to be pretty crazy down here. I think it's going to be even colder up there for you.

0:33 - Juan Vidri (Mvcvcapital)
  Yeah, yeah, I hear Saturday, Sunday, think we're going to be super cold. Let me, give me a second, let me see if Molly's coming.  Okay, yeah, she'll be here in two minutes.

0:56 - Ryan Cash (AcquiMatch)
  All right, sounds good. Let me see if I can figure out this deal file thing for you.

1:20 - Juan Vidri (Mvcvcapital)
  Okay. Yeah, I think it's weird because I do have access, I've had access to all the other ones except this one, so.

1:28 - Ryan Cash (AcquiMatch)
  It's in the same location as all the other ones.

1:35 - Juan Vidri (Mvcvcapital)
  Interesting. Okay.

1:43 - Ryan Cash (AcquiMatch)
  Hmm. Maybe? I don't know. It's there with everything else.

1:50 - Juan Vidri (Mvcvcapital)
  I just requested access again.

1:53 - Ryan Cash (AcquiMatch)
  Do you get a notification or anything like that? No. No. I mean, it looks like Ida is the owner of the entire folder.

2:08 - Juan Vidri (Mvcvcapital)
  Okay. She must be getting them then.

2:11 - Ryan Cash (AcquiMatch)
  But, I mean, you shouldn't. You shouldn't need to access it in the first place. So if you click this link, nothing, nothing pops up.

2:45 - Juan Vidri (Mvcvcapital)
  We'll see. No, it's just that you need access from Google Drive, so.

2:52 - Ryan Cash (AcquiMatch)
  Amazing.

2:54 - Juan Vidri (Mvcvcapital)
  Hey, Cash.

2:55 - Ryan Cash (AcquiMatch)
  Hey, Molly.

2:56 - Juan Vidri (Mvcvcapital)
  Late, fun, last-minute recording. from my boss, which is always a good time.

3:04 - Ryan Cash (AcquiMatch)
  Man. Well, we're trying to figure out deal files and why you're not able to access this one.

3:16 - Juan Vidri (Mvcvcapital)
  Maybe I'll try from Molly's computer. In the meantime, maybe she does have access to it.

3:22 - Ryan Cash (AcquiMatch)
  then maybe. Ah, okay, for some reason, it's changed to weird. I don't know if it was just copied over weird or what it looks like.  I can change it to, I guess it was restricted. existed. All just Bye-bye. Bye-bye.-bye. Bye. Bye-bye. Bye-bye. Bye Bye-bye.  Try it now.

4:06 - Juan Vidri (Mvcvcapital)
  There we go.

4:09 - Ryan Cash (AcquiMatch)
  Yeah, I don't know. For some reason, that one was restricted for only people with the, whose emails were listed in the Google Drive, and all the other ones were just anyone with the link could open it.  So that looks like it solved the problem. Yeah, that should be good to go. Yeah, and you can take a little bit of a deeper look at it.  It's a pretty simple, straightforward story, smaller on the SDE side. man. man. Thank But it's really consistent revenue, consistent SDE.  It's been at capacity and on repeat for a pretty good amount of time. Yeah, the average tenant is about 32 months.  Not really much customer concentration at all. Yeah, it's a good stable op. The only thing is, it is, yeah, just on the smaller side, deals in the area.

5:47 - Juan Vidri (Mvcvcapital)
  Yeah, okay.

5:49 - Ryan Cash (AcquiMatch)
  I'll take a look. Cool.

5:52 - Juan Vidri (Mvcvcapital)
  I think I read initially on this one, I was taking a look, like, in between meetings. It sounds like the SDE, I know.  Oh, it was on the lower side. But I think the other thing that eats into it is that I think we'd have to hire somebody to, like, maintain the day-to-day, which would be, like, 70K.  And so I think, like, post-debt, we would be making, like, maybe 100K from this one. So I don't, like, yeah, we'll look into it, but I honestly don't know if this would be a good fit, like, given the volume is so low.

6:30 - Ryan Cash (AcquiMatch)
  Is this the one you had to replace the GM?

6:33 - Juan Vidri (Mvcvcapital)
  Least-down structure?

6:35 - Ryan Cash (AcquiMatch)
  Yeah.

6:37 - Juan Vidri (Mvcvcapital)
  And I could have read it too fast or, like, misinterpreted, but I think it was, like, the current owner, like, runs the day-to-day operation, so they need to be replaced or something.

6:49 - Ryan Cash (AcquiMatch)
  I mean, you could also either just be the GM, right?

6:53 - Juan Vidri (Mvcvcapital)
  Yeah, but I don't want to work 40 hours a week doing it. So that's, I guess, the other side of it is, like, we could.  But then our goal was to not put in, like, we don't want to, like, buy a job. So, yeah, I think I'll take another look, but I do think even if we were, it would be making, like, $200,000, which doesn't even replace, like, my salary or your salary.  Like, I think this one just might be too low.

7:26 - Ryan Cash (AcquiMatch)
  Sure.

7:27 - Juan Vidri (Mvcvcapital)
  Yeah, and maybe Cash right now is the time to revisit what we have as a buy box because the last two deals, frankly, have not hit the mark in the that it's not what we're looking for, right?  And maybe right now it's, like, I'm frankly scared it would spend, what, four months and we've only sent two LOIs and I know it's a numbers game.  And so, to me, it's like, we need to be sending more LOIs, but the last two, for instance, one was retail and there was a huge...  Huge dependency on supplier and, like, I think a lot of the products were coming in from China. That's why, like, I look at Porter's 5 Forces.  That was one that, like, we were just at risk. And then the other one, can't remember what was the other one, the two latest ones.  Do you remember? The hot tub one. The hot tub one, the same issue, right? It was just one supplier who was supplying the hot tubs to this person in DFW, and then he would resell them.  Huge dependency on the supplier as well. And so I think right now we're at a point where we want to revisit what the parameters that you guys have in the search so that we can start looking at deals that probably fit more.  And also, if it helps, the other thing I was thinking about is, if we go upstream, meaning, we look at the pipeline that you guys have, and we can say yes, yes, no, no, no, yes, yes.  So that way you guys don't spend time talking to brokers or doing the analysis. But not on items or opportunities that we don't think will be a good fit for us.  And that would also speed up things, right? And that's what I guess I'm trying to say. It's like with Athena, when was it, like a month ago saying that the competitive landscape is even harder now.  A lot more people are buying businesses. Like, I want to hone in on our, like, buy box and also, like, figure out how to speed up the process.  And if that means, like I said, going upstream, I don't mind looking at what's in the pipeline. In fact, I would love to so that we can, like, at that point in time, we say yes, no, yes, no.  Again, that way we don't go in the rabbit hole and look at opportunities that probably are not a good fit for us.

9:54 - Ryan Cash (AcquiMatch)
  Okay, so there's a lot to unpack there. So going back. Back to the start of that. Yeah, mean, the reason that we're seeing these deals that are less complete is because we opened up, like, the SDE to try to get more deal flow to you guys, right?  And when you go lower on the SDE side, there's just going to be, by nature, more owner-dependence and a lot more elbow grease that is put into it, right?  So, I mean, if we don't want to see, if we're saying that we want to change that again and go back to deals that are, you 500 after debt or 400 after debt, if we can do that, it's just going to be less, like, there's going to be less deal flow in general, right?  Like, it's not, it's not too much work for us as well to, like, get these, you know, in front of you.  It's not like we, you know, there's not like a bottleneck of work that we can do or speed that we can run at.  I mean, And it is going to be less deals in general that go in front of you, which we can do.  It's just going to cut. It's just going to cut.

11:12 - Juan Vidri (Mvcvcapital)
  What's the SDU that you guys have right now on file for us?

11:15 - Ryan Cash (AcquiMatch)
  It's a minimum of $200 or $250 with, like, a flex to go down to, like, $200.

11:23 - Juan Vidri (Mvcvcapital)
  This is pre- After debt, post debt. Yeah. Yeah, think that's, okay, so pre-debt is $400, right? That's something at $50.  Depending on the price of the deal. Yeah, depending on the price. Yeah, yeah, Yeah. To me, that's too low.  But I don't know you. That's my first take on it. And I understand, to your point, it's going to be more owner-dependent as we go lower.  And honestly, for me, that's fine. It's just that, because we understand, right? great. great. They're less of an established company and it's more owner-dependent, and that's where we would come in and build systems, processes, and whatnot.  Yeah. I don't know. It's a hard one, right? Because it's the big three. Location, size, and industry. And if we're, like, set on location, DFW, then we need to be a little bit more flexible on size and industry, which we are an industry.  And size, I think, a little bit less flexible, but I don't want to go that low. Yeah. And I think the other part of it, too, is, like, yeah, we opened up the SDE range, and then that does give, like, more deal flow.  But I think we're also learning what we don't want through that. And so, like, that's where it's, like, maybe we revisit the deal box, like, now or in the future to say, okay, we actually don't want these, like, retail-oriented, highly supplier-dependent.  Yeah. Deals. Like, maybe that's the way we approach it because there could be, like, hidden gem that opens up where it's, like, yeah, there's owner dependence, but there's clear sight with, like, not a lot of cost associated with getting a number two in place that would allow us to not be there every single day and put in, like, 40-plus hours.  Like, I think that could still exist. So maybe it's just, like, we continue to curate the deal box with things that we know we don't want to do because now we're seeing them come here.  Like, I don't know. That's fair. I think as we look at these and I try to put myself in the shoes of, like, the owner, that's when I realized, oh, , I actually, this is not attractive to us, right?  Like, the trucking one, was really lucrative, but it was, like, something we wouldn't be able to do. Yeah, it was five businesses in one.  Yeah. So it's, like, we just have to know what we need. Or this hot tub one, right? Like, I, until I see the same, until I see, like, the, you know, the intricacies of the business, I...  I don't know that I don't want to be in that business, right? And so that's the hard part, and that's on us.  It's like, oh, . As we see these, we realize this is not what we want to do. And so I apologize for that in advance.  It's just we're learning as we go, right?

14:17 - Ryan Cash (AcquiMatch)
  No, 100%. Everyone, every single person goes through the same set of things, right? I promise you, there's nothing wrong with you, and everything is normal.

14:30 - Juan Vidri (Mvcvcapital)
  Thank you, I'm very sure. Because I feel like we go back and forth and stuff, but it's like, until we see that, we realize, like, I try to put myself in the owner's shoes and see if, like, I'm willing to do that.  And frankly, some yes, some no, right? Yeah, like, this one, like, I wouldn't see myself going and, like, forklifts.  Like, I could do it. I would do it for the right price. But, like, I think if we're only going to be making that, like.  Like, you know, $150,000 after. Like, I'd be replacing my job with a downgrade. You know what I mean? So it's like, I think, yeah, that's where we just maybe, yeah, update the buy box as we come across these opportunities.  We know that we just won't pursue. And also, Cash, just a quick question. I know that Karis, before leaving, she was a lead on off-market.  And I remember her saying that we would start getting off-market probably at month two. Do we know, do you know if someone else has picked that up, like the off-market deals?

15:34 - Ryan Cash (AcquiMatch)
  Yeah, we have someone doing off-market. Right now, maybe, like, five to ten percent of, like, our total deals is off-market, which is about the same as what it was when Karis was running it.  I see. That is, like, also our, I mean, our biggest initiative. is to, by the of this year, for Aquamatch, get that up to one out of three, so one out of two deals for us.  And there's a lot of, there's a lot of stuff in the background that are levers and things that Athena is pulling to get that ramped and launched and scaled, I should say.  But yeah, as of now, it's like one out of, I'd one out of ten. We've got two clients who are under offer on off-market deals at the moment.  It's just a little bit of a dice roll on the off-market stuff.

16:41 - Juan Vidri (Mvcvcapital)
  Yeah, yeah, for sure. And fun fact, yesterday I was skimming through BizBuySell, and guess who I saw as a listing broker?

16:49 - Ryan Cash (AcquiMatch)
  Is it Karis? Yeah. Yeah, I talked to Karis, have messages, like, from Karis on WhatsApp, like, right now. Yeah.  That's what it's today, yeah. No, no, we talked. She's running deals. She's running, started up her own sell site.  I think it's like her own thing. Like, she's running her own. That's amazing.

17:11 - Juan Vidri (Mvcvcapital)
  I saw a, I was looking at a listing, and I scrolled down, and you know how you can see the broker on the right?  I saw a picture that I recognized, and it's the exact picture that she used in Slack here.

17:22 - Ryan Cash (AcquiMatch)
  And so I was like, oh, that's curious. Was it a Dallas deal?

17:26 - Juan Vidri (Mvcvcapital)
  Yeah. Well, it was remote. think it was at a, they were, they were in North Carolina, but it was a remote business.  It's a marketing agency, SEO. In Dallas. It was a Dallas listing. It was, okay. It was a Dallas listing.  It was remote.

17:43 - Ryan Cash (AcquiMatch)
  was. Did y'all jump into it, or what?

17:45 - Juan Vidri (Mvcvcapital)
  You're gonna. No. Absolutely not. No. FYI, you know this. AI is completely rocking the SEO world. Like, everything that SEO was has now just, like, flipped on its head, and everyone is.  Scrambling all companies to figure out how to get in the AI space. So when I see SEO is up for sale, I'm like, oh, they probably got tired of dealing with the disruption, and they went out at this time.  So all that to say, SEO, we can probably add that to the buy box. We don't want to do that.

18:16 - Ryan Cash (AcquiMatch)
  Yeah, I already have. I understand your lack of desire for marketing or marketing agencies in general, Molly. I've got that one all listed on our front.  Although I think you'd be great. I think for the right opportunity, be phenomenal.

18:33 - Juan Vidri (Mvcvcapital)
  The thing is, it's scary because I keep seeing posts on LinkedIn of how AI agents are now doing what these marketing agencies can take forever, but an AI agent with just a prompt can do a lot of things that they do.  so that's what's scary. Now, staying at the forefront of that, like if a marketing agency is staying at the forefront and they're like the pioneers of that, that's probably different.  But I don't think we are AI experts to be able to do that, you know?

19:05 - Ryan Cash (AcquiMatch)
  I think it's also like, that is such a, I'm sure Molly could also write a dissertation on this, like marketing agency is like such a wide range of things that it's kind of like a word that almost doesn't make sense to use because it can mean like a million bajillion different things.  Yeah, think within that, like, there's stuff that is cool and viable and interesting. There's also stuff in that that's like completely replaceable already that isn't good.  But I think in general, like, there's still, depending on like high, how high level, like, and how, how involved is the AI.  Agency and, like, overall strategy and how involved, like, what type of client base are they serving? Like, there was an agency that was pretty cool out of Atlanta that I was looking at for some clients in Atlanta, and they just worked with NFL teams, and they ran the entire sports team's, like, marketing book, everything from high-level strategy to, they even will print out the little, like, cutouts of the players that go in front of, like, you know, the ticket booth, like, as people walk up, so, like, and their retainer was, like, $100,000 a month, you know, it was, like, a whole thing, you know?  So, like, I think stuff like that is incredibly viable. That one was, ended up being a bad deal because they had three owners who ran the entire company, and they were trying to sell it.  Thank you. Without having really replaced themselves, which was not optimal. But stuff like that, yeah, sure.

21:09 - Juan Vidri (Mvcvcapital)
  That's cool. It has a pulse.

21:11 - Ryan Cash (AcquiMatch)
  That's value.

21:12 - Juan Vidri (Mvcvcapital)
  Just watch it by a marketing agency, whatever you want to call it.

21:17 - Ryan Cash (AcquiMatch)
  That would be funny. Juan and Molly walk into a room determined to buy anything but a marketing agency. Juan and Molly walk out with a marketing agency.

21:32 - Juan Vidri (Mvcvcapital)
  Juan is hilarious. Anyway, I wanted to show you, oh man, did it bug me off already? Benchmark? Yeah.

21:42 - Ryan Cash (AcquiMatch)
  Yeah, okay.

21:43 - Juan Vidri (Mvcvcapital)
  That was something I needed to connect with you on because I went, was that something that you had or was that one that we sent you?
  SCREEN SHARING: Juan started screen sharing - WATCH: https://fathom.video/calls/540627270?timestamp=1309.83703  I think it's one that we sent you guys.

21:54 - Ryan Cash (AcquiMatch)
  Okay, because I sent over like signing an NDA, right? Dude, I spent all day. Dude, Sending these connections for Benchmark, and it's such a pain.

22:04 - Juan Vidri (Mvcvcapital)
  Yeah, so I think it's one that we sent, and then they sent us back an email asking us to sign the NDA, or to go into Benchmark, create a profile.

22:15 - Ryan Cash (AcquiMatch)
  Yep, that's how they do stuff.

22:17 - Juan Vidri (Mvcvcapital)
  Yeah, it was a broker sent just to me and Molly. So I created a profile, I updated our stuff there, and then after that, they were like, oh yeah, I'm going to ask the seller, we'll take a look to see if he wants to release a SEMP.

22:35 - Ryan Cash (AcquiMatch)
  That's bench mode.

22:36 - Juan Vidri (Mvcvcapital)
  called me yesterday, yeah, and then yesterday afternoon, they were like, yes, the seller has agreed to release a SEMP.  And this is what I'm showing you right now, it's actually like on the landing page, it's not a PDF, it's like on a landing page.  So that's why I was, so I don't care, but all the info is here.

23:00 - Ryan Cash (AcquiMatch)
  Hey, so the way Benchmark works, like, they have a set process for buy-side advisors. I have my own Benchmark log in.  They can associate our accounts together on their system so that I can also get access. It's, um, could you respond to the broker?  And I have two weeks that I have my Benchmark set up. I have a separate email to manage all of this deal flow stuff because it is, like, an entire thing.

23:40 - Juan Vidri (Mvcvcapital)
  Yeah, I would, because every time I type in cash here, I get two emails, so I was debating.

23:48 - Ryan Cash (AcquiMatch)
  Yeah, if you could, there's one that's Ryan.cash. Oh, it's on there. That's the one you use. Awesome. Could you, uh, respond to that email to the broker and say, hey, this is...  Like, this is my by-side advisor, he already has the benchmark count, can you please give him access to the deal.

24:12 - Juan Vidri (Mvcvcapital)
  Yeah, I can definitely do that. And just the high-level, I guess I'll show you, this is what they do, they do roofs in the DFW Metroplex.  Those are some fancy roofs. Yeah, what I see, these are, like, metal, fancy roofs for extremely wealthy customers. Sure, look at that, that looks like a castle.  I know. Yeah, these are. Let me get one of those, yeah. This is where they operate out of, which it is completely different.  Let me show you, okay, these are the financials. 24, okay, TTM, okay, so. 24. 24. 24. Oh, it's hot.  No, but this is fall, so this is 8 p.m. 8.m. October, 2025. Could be that. It was season. No, October number, December is hot.  Yeah, correct. Seasonality. Could be seasonality.

25:13 - Ryan Cash (AcquiMatch)
  Uh, yeah, I'm not sure it's like roofing.

25:16 - Juan Vidri (Mvcvcapital)
  It's like project-based.

25:18 - Ryan Cash (AcquiMatch)
  Yeah. These numbers do not, like, fluctuate enough for me to be paired.

25:25 - Juan Vidri (Mvcvcapital)
  Okay. Yeah, everything here seems pretty straightforward. Um, there's two owners. There's two owners who are willing to sell. The only concern, I guess if you want to call it a concern, have it, it's that it's an prospect, so it's like an hour and a half away from us, right?  Um, but I guess we can rent it.

25:49 - Ryan Cash (AcquiMatch)
  No, no, no, they own this.

25:51 - Juan Vidri (Mvcvcapital)
  Sure. And so, I don't know, they just use it to meet clients there, which if we needed to, I'm assuming...  We could move it. But anyway, take a look.

26:06 - Ryan Cash (AcquiMatch)
  No, mean, let's talk through a couple things right now. So I can tell you the biggest thing with this, being a roofing company in Texas, it's going to be licensing, licensing.  Did they state anything about the roofing license? So, look, it's going to be the biggest thing where, like, you have to have a license to install a roof in Texas.  And we need to find out, are the owners the people who have the licenses? Are there any key employees who have licenses?  And if there are key employees, like, are they willing to stay on, or will we need to, like, hire a replacement?

26:56 - Juan Vidri (Mvcvcapital)
  We would have to hire because there's only two employees.

28:00 - Ryan Cash (AcquiMatch)
  22% revenue here, so it means that I find it hard to believe that with that revenue profile, like, there's, man, there's no way someone, one person paid them $700 million for one roof, right?

28:16 - Juan Vidri (Mvcvcapital)
  If it is, I want to see the house. Yeah, yeah.

28:19 - Ryan Cash (AcquiMatch)
  I'm not saying Dallas, you're out of question, right? Like, I think there's probably a house somewhere in Dallas that would cost $700,000 to roof it, but, like, in general, that...

28:32 - Juan Vidri (Mvcvcapital)
  It is, some people have multiple homes, and I think this is just the, there's a growth opportunity section somewhere in here, and it talks about expanding to commercial.  So, I actually don't think they fully tapped commercial at all, here, or, like, featured.

28:50 - Ryan Cash (AcquiMatch)
  Yeah. Okay, well, that ends up being a better thing for me. I'm telling you, like, something was commercial on that one client, though, right?  Something's also just... Weird. Like, these numbers are huge. Like, client number two was 8.1% of total revenue. You're telling me that one of these houses cost $300,000 to roof?

29:11 - Juan Vidri (Mvcvcapital)
  That's so fair.

29:12 - Ryan Cash (AcquiMatch)
  That's true. Like, there's no way. Like, there's no way. It shows me it's got to be a commercial project.  Or it could be that it's a builder. It could be doing that they're doing new residential builds and that that one builder contributed to multiple houses, right?

29:36 - Juan Vidri (Mvcvcapital)
  like it. Management notes that less than 10% of real revenue is attributed to repeat clients, as most repeat clients are from individuals with multiple properties needing roofing services.  Yeah.

29:49 - Ryan Cash (AcquiMatch)
  Okay, so here's, look, I know, like, series of thoughtfulness because I went through a really similar deal in San Antonio.  Like, I think the biggest thing on this deal is going to be more. For, like, qualitative, you need to understand, does this guy have an actual sale and marketing channel where he's capturing new work, or is he an old boy sitting at a country club pulling leads at the bar?  Like, that is going to be the biggest thing that's going to contribute to, like, whether this is, like, a real business, or if this is...

30:31 - Juan Vidri (Mvcvcapital)
  So, according to this bullet point that I'm highlighting, you can barely see it, but it says, the company secures new clients from SEO, marketing platform, social media presence, and referral pipeline.  And so, seems to be... More of, like, an established company. don't know how much they're tapping into that.

30:52 - Ryan Cash (AcquiMatch)
  In fact, we can look... I it. I'm just saying, like, in terms of diligence, like, the owner, the sales guy owner...

31:00 - Juan Vidri (Mvcvcapital)
  100% involvement in the sales process and how they're pulling these clients and especially is a lot more of a important thing if they're builders.

31:09 - Ryan Cash (AcquiMatch)
  If it was independent, if it really is independent homeowners, it is better. If it's builders, that becomes a bit more tricky to hand over those relationships.

31:26 - Juan Vidri (Mvcvcapital)
  Yeah. And plus the concentration risk there is higher because one builder might manage, like you said, 20%, right? And so anyway.

31:35 - Ryan Cash (AcquiMatch)
  If we need a new build, then you're tied into the real estate market growth in general. But if they're really putting roofs on a lot of different houses and the owners have multiple properties, basically if it's remodel money, then that's less risky and less exposed to just the general real estate.

32:00 - Juan Vidri (Mvcvcapital)
  Got it. I'll send that email to the broker, Cash. We need to run to daycare pickup, but yeah.

32:07 - Ryan Cash (AcquiMatch)
  I lost track of time. How could I forget? We've got the daycare pickup. Well, look, I know you have to run.  You'll have to get the kids. Let us do this. I'm going to please send that email over, try to get me access to this so I can do a deep dive and the team can do a deep dive and do our own report on this op for you.  I would still request a call with the broker or the owner. And let's, if we need to, we can set up an ad hoc call sometime like earlier next week to go through any updates or anything we need to.

32:56 - Juan Vidri (Mvcvcapital)
  Appreciate it, man. Thank you so much, Cash.

32:59 - Ryan Cash (AcquiMatch)
  Yes, thank you. All right. Y'all stay warm.

33:02 - Juan Vidri (Mvcvcapital)
  It's going to get cold. You too. Yeah. You too. Good luck. Bye. All right. Bye, man. Bye.




"""




internal_profile="""

{
  "1) Client Overview & Status": {
    "Client Name": "Juan & Mollie Vidri",
    "Search Start Date": "October 1, 2025",
    "Location (Home Base)": "Fort Worth, Texas (Aledo/Fort Worth border)",
    "Timezone": "Central Time (US/Central)",
    "Current Status": "Existing owners (short-term rental business) actively searching for their first ETA acquisition with AcquiMatch. First LOI submitted November 2025 on a DFW electrical services company but not selected to advance. Continuing search with expanded industry scope including select tech/digital categories while maintaining SDE and DFW-first guardrails.",
    "Decision Makers": "Joint decision by both Juan and Mollie; either can veto; both must say \"yes\"",
    "High Level Important Note": "Pre-qualified with Live Oak up to $7.75MM; DFW-first search with openness to remote operations; strongly avoid tech/online businesses due to AI risk; target income replacement of ~$550–$600K; willing equity injection ~$300K (plus AcquiMatch fee)",
    "Profile Maintained By": "Ryan Cash (Analyst) | Last Updated: 2025-12-10",
    "Logs": [
      "August 11, 2025 — Juan Vidri Intro Call",
      "August 12, 2025 — Juan Vidri Exploration Call",
      "August 19, 2025 — Juan & Mollie - Meet & Greet",
      "September 05, 2025 — AcquiMatch Buyer Discovery Call Juan & Mollie Vidri",
      "September 12, 2025 — AcquiMatch Dealbox Discovery Mollie & Juan",
      "October 14, 2025 — Weekly Check-in; NDA Walkthrough; Review First Write-up",
      "October 23, 2025 — Weekly Check-in",
      "October 28, 2025 — Weekly Check-in; Analyst Transition",
      "November 04, 2025 — Weekly Check-in; Electrical Services Deal Review",
      "November 11, 2025 — Weekly Check-in; First LOI submitted",
      "November 18, 2025 — Weekly Check-in; LOI status follow-up; industry scope expansion discussion",
      "November 19, 2025 — Search scope expansion details",
      "November 24, 2025 — Electrical Services LOI outcome",
      "December 04, 2025 — Glazier/Blinds update",
      "December 09, 2025 — Weekly Check-in; new CIMs received; discussed revisiting trucking/logistics",
      "Slack Conversations from the beginning"
    ]
  },
  "2) Search Parameters": {
    "Client Intro": "Juan and Mollie are seasoned product marketing and business leaders with more than two decades of combined experience in fintech, marketing, financial services, and growth. They have built and launched multi-billion-dollar payment products at Fortune 100 companies, directed cross-functional teams, and driven customer acquisition strategies, showcasing their ability to innovate and scale at the highest level. Beyond corporate leadership, they have entrepreneurial experience in real estate investment and short-term rental operations, where they successfully managed properties and built operational teams.",
    "Target Business Size": [
      "SDE: Minimum $750,000",
      "Enterprise Value: Up to $10,750,000 (aligned to SBA pre-qualification of $7,750,000 plus $3,000,000)."
    ],
    "Geography": [
      "Primary: Dallas–Fort Worth, Texas",
      "Nearby: North Texas corridors as practical.",
      "Flexibility: Open to remote or multi-location operations if day-to-day can be led locally.",
      "Note: Geography is not listed on the external profile. This reflects internal guidance from calls and does not change any public items."
    ],
    "Industry Approach": [
      "Top interests: High-touch service businesses, manufacturing, niche printing, insurance models, home health care, and companies with recurring revenue.",
      "Strong NOs: Restaurants, oversaturated industries or trend-driven models, complex compliance industries, businesses requiring specialized licenses, advertising, high-technology and media businesses, and low-touch models with high-risk volatility.",
      "Online stance: Prefer tech-light, operational businesses; avoid high-technology and media businesses.",
      "Internal pilot additions (Nov 19, 2025; external profile unchanged): Testing select tech/digital categories to increase deal flow — MSPs, cybersecurity/compliance, ISPs, POS/IT integration, and network cabling/telecom. SDE and DFW-first guardrails still apply."
    ],
    "Business Characteristics": [
      "Stable operations with strong, consistent cash flow and clean, scalable processes.",
      "Clear growth opportunities and customer retention levers.",
      "Existing team in place; ideally includes a strong number two.",
      "Customer model: B2B preferred or recurring customer bases; B2C is acceptable if operations are stable.",
      "Avoid heavy regulation and businesses that need specialized licenses."
    ]
  },
  "3) Financial Profile (internal only)": {
    "Minimum CashFlow/Income (Pre-Tax) After Debt Service Desired": "$550,000 to $600,000 (household)",
    "Minimum CashFlow/Income (Post-Tax) After Debt Service Desired": "Not specified",
    "Ideal Cashflow/Income (Pre-Tax) After Debt Service Desired": "Needs confirmation",
    "Ideal Cashflow/Income (Post-Tax) After Debt Service Desired": "Not specified",
    "Total Cash Available": "Not specified (liquid funds today)",
    "Planned Investment Amount": "$300,000 excluding AcquiMatch fee; $400,000 including the AcquiMatch fee",
    "Net Worth": "Approximately $1.3 million (Needs confirmation)",
    "Financing Plan (if strong preferences)": [
      "Primary: SBA 7(a) with ~10% equity injection, plus a seller note on standby when possible. Target DSCR near 2.0 and prefer valuations at or below 4x. Open to using the Barlow & Williams standby structure to count a small seller note as equity injection when needed.",
      "Alternatives: Open to a private capital partner that provides debt and minority equity (e.g., Stonehenge) to increase purchasing power. Considering a HELOC on a rental property to bolster the down payment and limit personal guarantee exposure. Do not want to use ROBS (would only consider as a last resort “unicorn” case).",
      "Seller rollover equity: Open to structures where the seller retains a small minority stake (around 10%) to keep alignment; needs confirmation on SBA rules and whether a seller PG would be required.",
      "Real estate: Open to buying the property with longer amortization (up to ~25 years) or leasing instead; may hold the property in a separate real estate entity and have the operating company pay rent. Will decide based on modeling and lender guidance."
    ],
    "Bank / Lender Relationships": [
      "Live Oak Bank (primary contact: Wendy Ghormley, CPA); prior contact Rebecca at Live Oak"
    ],
    "Prequalification Status": "Pre-qualified up to $7.75MM with Live Oak Bank (letter dated 09/23/2025)",
    "Financial Guardrails": [
      "Must replace $550,000 to $600,000 pre-tax household income from the business after debt service.",
      "Target DSCR close to 2.0x.",
      "Prefer to keep purchase multiples at or below 4x; may consider higher only for exceptional, remote, low-time businesses.",
      "Do not want to use ROBS.",
      "Seek to limit personal guarantee exposure; prefer not to pledge the primary residence; exploring HELOC on rental property to position liens ahead of SBA.",
      "Comfortable equity injection range: $300,000 to $400,000 (including fee at the top end).",
      "Do not want to take on additional loans for large build-outs tied to a deal; avoid big development projects at or right after close.",
      "Prefer SBA loan size at or below $5,000,000 to avoid stretching the 10% equity injection."
    ],
    "Comfort with Financial Risk": "Conservative to moderate. Numbers-driven and risk-averse, they prefer strong cash flow, lower leverage pressure, and a safety margin over paying up for growth."
  },
  "4) Business Characteristics (internal-only detail)": {
    "Preferred employee count / team structure": [
      "Comfortable leading 10 to 40 employees directly or through managers.",
      "Strong preference for a proven number two in place or a lead manager they can develop.",
      "Fine with front-line blue-collar teams; Juan speaks Spanish and is hands-on in the field when needed.",
      "They can rebuild hiring, training, and performance systems if needed.",
      "Avoid one-person owner-operator businesses that require building the whole team from scratch.",
      "Open to the seller staying on as a #2/GM or sales lead if EBITDA supports a fair market salary.",
      "If the seller stays on, their pay should be covered by SDE or offset in price/structure (for example, a performance note)."
    ],
    "Customer base preferences": [
      "Prefer B2B or recurring customer models. B2C is fine if operations are stable and repeat-driven.",
      "Want low to moderate competition in the local market.",
      "Prefer a diversified book. Internal guideline: avoid heavy concentration. Ideally no single customer above 20 to 30 percent of revenue.",
      "Cautious about referral or channel concentration above about 40 percent."
    ],
    "Growth profile": [
      "Target stable, steady businesses with clear growth levers.",
      "Like “fix and grow” work such as digitizing, adding CRM, pricing, better marketing, adding services, and light add-ons.",
      "Do not want heavy turnarounds, distressed situations, or “fire drill” growth where a competitor forces constant urgent action.",
      "Open to fragmented sectors with add-on potential when the first platform is focused and stable."
    ],
    "Sales/marketing intensity tolerance": [
      "Very strong on marketing strategy, lifecycle, and brand refresh. Comfortable implementing CRM, websites, and performance marketing.",
      "Comfortable with relationship sales, account management, quoting, and negotiation.",
      "Prefer inbound or warm pipeline models. Light outbound is fine.",
      "Avoid models that need heavy cold-calling, door-to-door, or “boiler room” new-logo hunting to hit numbers.",
      "Prefer sectors where the marketing plan is clear to them; they will pass if they cannot see simple, practical marketing levers to pull.",
      "If evaluating a marketing agency or digital service, prefer strategic, retainer-based work for durable niches over production-only work that AI can replace; require a strong GM/lead so they are not “buying a job.”"
    ],
    "Operational complexity": [
      "Prefer single-site or multi-site with simple, repeatable routines.",
      "Field operations are okay if routes and schedules are predictable.",
      "Hybrid or partially remote operations are a plus. Fully remote is fine if not tech-centric and if controls are strong.",
      "Early months: they will be hands-on; longer term they want a manager-led day-to-day.",
      "Open to operations 2 to 3 hours from home if the team is self-sufficient and visits can be planned after the first few months.",
      "Prefer focused businesses over “several businesses in one.” Will avoid multi-line setups that mix unrelated units (e.g., ops plus new retail, fuel, and real estate) for their first deal.",
      "Do not want large new build-outs tied to the deal or extra loans for development projects at or right after close.",
      "Comfortable entering licensed trades when a master license holder is in seat or can be hired before or at close; will make retention or hiring of that licensed leader a condition to proceed.",
      "For agency or digital service models, need a manager/lead in seat and a retainer-based client mix so daily work is not owner-dependent.",
      "For IT managed services or infrastructure businesses (MSP, cybersecurity/compliance, ISP, POS/IT integration, network cabling/telecom), prefer recurring contracts and SLAs with a manager-led team; avoid heavy one-time project revenue and pure software products"
    ],
    "Asset-heavy vs. service-based": [
      "Prefer service-based or light to moderate asset models.",
      "Comfortable with equipment fleets or shop-based assets if capex and maintenance are predictable and do not crush cash flow.",
      "Open to light manufacturing and niche printing where assets are important but manageable.",
      "Open to asset-light distribution with little or no inventory when operations are stable, remote-friendly, and not highly exposed to AI/online risk.",
      "Interested in capital-light, home-based platform or aggregator models that connect services (for example, vendor-to-contractor networks) if tech-light, defensible, and not exposed to AI/online risk."
    ],
    "Cultural fit": [
      "Values integrity, happy teams, and a collaborative, low-ego culture.",
      "Strong preference for buying from a retiring owner who will not compete post close, or a younger “builder” who will sign a solid non-compete; open to the seller staying on in a commission-based sales role or stepping into a #2/GM role to reduce competition risk and help with knowledge transfer.",
      "Respect seller legacy and local reputation. Will keep key staff and strengthen systems.",
      "Mission and community impact matter. They want work that feels meaningful, not just profit.",
      "Prefer responsive, organized sellers and brokers who provide timely, clean YTD/TTM financials; slow or disorganized processes reduce trust."
    ],
    "Hidden NOs / soft preferences": [
      "Avoid high-pressure competitive markets where a rival forces constant reaction.",
      "Avoid trend or fad models and low-ticket, high-volume retail.",
      "Avoid online-only, SaaS, media, and digital agencies due to AI risk.",
      "May consider select marketing agencies only when they do high-level strategy on retainers for durable niches and have a GM/lead in place; will still avoid production-only, AI replaceable work.",
      "Avoid heavy regulation or specialized clinical care that requires deep medical oversight.",
      "Avoid businesses that require the owner to hold a long-path license to operate, like master plumbing, unless a licensed leader is already in place or can be hired before or at close.",
      "Avoid very inventory-heavy retail and e-commerce with copycat risk and race-to-the bottom pricing.",
      "Prefer recurring revenue, insurance-billed models, and stable B2B services with room to modernize.",
      "Prefer strong non-compete protections with sellers, especially when the seller is younger and could restart a competing shop.",
      "Avoid one-man shops or solo owner-operator models with no team in place.",
      "Backlog or booked work runway is a plus (helps with stability and planning).",
      "Avoid complex, multi-line “conglomerate” deals (e.g., trucking plus repair, retail, fuel, and real estate) for the first acquisition.",
      "Avoid deals that require large capital projects at or right after close, or extra loans for buildouts.",
      "Prefer industries where they can quickly apply their marketing playbook; will pass when the marketing path is unclear to them.",
      "Slow or disorganized sellers or brokers who cannot provide timely updated financials (YTD/TTM) reduce confidence and are a soft pass risk.",
      "Avoid pure SaaS or software product companies and IT shops with project-only, lumpy revenue; prefer MSP-style recurring contracts if considering tech/digital services."
    ]
  },
  "5) Professional Background": {
    "Career Overview": [
      "Juan and Mollie are senior operators with 25+ years combined experience in payments, fintech, airlines, e-commerce, and marketing. They've built and launched credit cards and loyalty programs at Amazon, eBay, and American Airlines, and currently own and operate Little River Cabins, a 4-cabin short-term rental business where revenue has grown 50% year-over-year since purchase."
    ],
    "Industry Exposure": [
      "Payments and financial services (credit cards, digital wallets, loyalty programs).",
      "Airlines and travel (American Airlines; SMB loyalty; international co‑brand programs).",
      "E‑commerce and retail (Amazon, eBay, Pier 1).",
      "Digital marketing and CRM (agency and in‑house).",
      "Real estate and hospitality operations (short‑term rentals)."
    ],
    "Functional Strengths": [
      "Finance: Juan managed $475M airport budgets, built financial models for Latin America portfolios, and negotiated budgets across 40+ countries. Both analyze deals using cash flow models, DSCR calculations, and scenario planning. They review broker models critically and understand lease-versus-buy decisions for real estate.",
      "Product Management: Juan led product roadmaps for Amazon's billion-dollar loyalty program,  defined success metrics, and reported to senior leadership. Mollie led product marketing for gift cards and payments at major retailers.",
      "Marketing: Juan launched credit cards at Amazon and eBay, managing customer acquisition and lifecycle programs. Mollie led global demand generation teams of 26 people, built customer segmentation, and drove double-digit revenue growth through testing and optimization.",
      "Operations: They manage their rental business end-to-end, including field teams, maintenance vendors, and same-day problem resolution. Juan implemented revenue management software and built operational processes from scratch.",
      "Partnerships: Juan negotiated multi-year bank contracts worth $73M and managed international partnerships. Mollie secured high-visibility partner placements and created new revenue streams.",
      "People Management: Mollie has managed teams up to 26 people with 6 direct reports, handling hiring, coaching, and performance management. Juan led cross-functional teams across engineering, design, marketing, and analytics.",
      "Field and Blue‑Collar Readiness",
      "Juan speaks Spanish as a first language and is comfortable working with field crews and trades.",
      "Both will be on site early to learn and stabilize, then will build manager‑led operations."
    ],
    "Leadership & Management Experience": [
      "Team scope: Mollie led 26 people (6 direct reports) at Square; previously managed 4–6 at Amazon and Pier 1; led cross‑functional work across 10+ regions. Juan managed 3–4 directs and cross‑functional pods of 8–9, plus 5 engineers; led partner and vendor teams across Latin America.",
      "Budget scope: Mollie managed $20–30M annual marketing budgets and secured $17M+ incremental funding; Juan controlled $475M+ airport budgets and created a $145M international co‑brand budget across 100+ products.",
      "Decision scope: P&L accountability for marketing programs, product feature roadmaps, partner negotiations, contract renewals, and performance targets; built and approved BRDs, pricing and promo plans, and portfolio strategies.",
      "Remote leadership: Have led and operated teams remotely for about five years; comfortable running distributed operations and weekly cadences."
    ],
    "Unique Abilities (Superpowers)": [
      "Turn chaos into clear routines and SOPs fast.",
      "Make numbers simple and actionable; build models that drive decisions.",
      "Negotiate with calm, data, and patience to reach better terms.",
      "Build happy, high‑performing teams; coach people to grow.",
      "Spot growth levers quickly (pricing, segmentation, CRM, add‑on services).",
      "Stand up brand and demand engines that drive steady, repeatable revenue.",
      "Solve hard problems under pressure and keep customers whole.",
      "Bridge office and field; work in Spanish and English with any crew."
    ]
  },
  "6) Development Areas": {
    "Skills gaps needing support": [
      {
        "Skill gap": "Diligence questions and red flags beyond the surface",
        "Identified by": "self-identified",
        "Description": "Mollie said she is learning what to ask and wants help spotting issues sellers may not share. Without this, they could miss hidden risks."
      },
      {
        "Skill gap": "Financial analysis confidence for Mollie (P&L tie-outs, ad backs, DSCR)",
        "Identified by": "self-identified",
        "Description": "Mollie can work with numbers but does not enjoy them and wants to grow here. She asked for help learning what to look for in CIMs and P&Ls."
      },
      {
        "Skill gap": "Working capital, inventory, and cash cycle modeling",
        "Identified by": "self-identified",
        "Description": "Juan asked for help on working capital (including seasonal needs) and wants to avoid mistakes he has seen other buyers make. They want support to size cash buffers and avoid a liquidity crunch."
      },
      {
        "Skill gap": "Financing structure depth (SBA rules, seller notes on standby, equity injection tactics, PG and HELOC strategy)",
        "Identified by": "self-identified",
        "Description": "Juan asked detailed questions on SBA changes, standby seller notes as equity, using a HELOC, and minimizing the personal guarantee. He also wants clarity on seller rollover equity under SBA (e.g., if a seller keeping ~10% must personally guarantee) and the 51% control rule. He wants guidance to choose a safe, bankable path across SBA vs private capital. On Nov 11, he asked how their $7.75MM prequal relates to the SBA $5MM cap and how pari passu lending works; he wants lender-specific guidance on which banks do it and how terms vary."
      },
      {
        "Skill gap": "Private capital option evaluation (minority equity + debt “PE-lite”)",
        "Identified by": "self-identified",
        "Description": "After the Stonehenge session, Juan realized this path can work and wants help comparing it to SBA so they can raise their purchasing power when it makes sense."
      },
      {
        "Skill gap": "Real estate buy vs lease and OpCo/PropCo structure modeling",
        "Identified by": "self-identified",
        "Description": "Juan said he is on the fence and wants to model both paths and get lender guidance. He mentioned using a separate real estate entity with rent from the operating company. They need support to compare DSCR, taxes, and cash impact for each option"
      },
      {
        "Skill gap": "Operational diligence on hidden costs and vendor churn",
        "Identified by": "self-identified",
        "Description": "From the cabins, they learned about surprise costs and losing key vendors. They want help building a checklist to uncover these risks before close."
      },
      {
        "Skill gap": "Search focus and deal selection discipline (avoid “getting hyped over anything”)",
        "Identified by": "self-identified",
        "Description": "They can get excited by many businesses. Mollie is actively slowing same-day LOIs and asking to meet the next day before moving. They want help staying “sniper,” not “shotgun,” so they do not drift from their criteria."
      },
      {
        "Skill gap": "Delegation and workload boundaries for Mollie",
        "Identified by": "self-identified",
        "Description": "Mollie said she takes on too much and can burn out. She wants support to plan work split, delegate early, and protect focus during search and integration."
      },
      {
        "Skill gap": "Decision pacing for Juan (pause-to-plan before acting)",
        "Identified by": "self-identified",
        "Description": "Juan said he needs to practice patience and tends to push LOIs fast. He has improved and wants a pause step with pre-mortems and checklists to keep decisions thoughtful."
      },
      {
        "Skill gap": "Pre-LOI offer strategy and process confidence",
        "Identified by": "self-identified",
        "Description": "On Nov 4, Juan asked for reassurance about when to send an LOI and how much to validate before it. After hearing that LOIs open the books and lenders act as an early QoE check, he agreed to move fast, schedule the broker call with Mollie, and prep the LOI. He wants help using this pacing on “hot” deals without over-analyzing first. On Nov 7, he also asked how to reach the final table without offering too much; he wants guidance on pricing anchors and when to flex multiples in competitive processes."
      },
      {
        "Skill gap": "Decision-making with incomplete information (70–80% pre-LOI)",
        "Identified by": "self-identified",
        "Description": "On Nov 11, Juan said he needs to get comfortable making decisions with 70–80% of the data when timelines are short. He wants simple checklists and guardrails to move fast while managing risk."
      },
      {
        "Skill gap": "Seller readiness and trust signals during the process",
        "Identified by": "self-identified",
        "Description": "On Nov 11, Juan said slow or messy YTD/TTM updates reduce his comfort (blinds/glazier example) and that they “need to put more emphasis” on trust and responsiveness. They want a short set of cues to judge seller readiness, organization, and fit early."
      },
      {
        "Skill gap": "Market and buyer-pool signals (is low competition a red flag?)",
        "Identified by": "self-identified",
        "Description": "On Dec 09, Juan asked if the lack of PE interest in a $1.2M SDE trucking/logistics deal should be seen as a red flag. He wants help reading buyer-pool patterns by industry and how to weigh them in go/no-go calls."
      },
      {
        "Skill gap": "SBA bankability screen for project-heavy, lumpy revenue (recurring vs projects; sales team present)",
        "Identified by": "inferred by system",
        "Description": "On Dec 09, a hotel lighting manufacturer required all-cash after two SBA declines due to lumpy project revenue and no sales team. They need a quick bankability checklist to flag these patterns early so they avoid time on deals lenders will not finance."
      },
      {
        "Skill gap": "Licensing and regulatory plan for licensed trades (electrical, HVAC)",
        "Identified by": "self-identified",
        "Description": "In the Nov 4 electrical deal, Juan said the deal would be contingent on a master electrician passing and staying, or hiring one from outside. They want help mapping license options, timelines, and making the license-holder plan and related terms part of the LOI/APA."
      },
      {
        "Skill gap": "100-day post-close integration plan and change management",
        "Identified by": "inferred by system",
        "Description": "As first-time ETA buyers who want to “learn and maintain” and not tinker too much, they will benefit from a clear day-30/60/90 plan, role split, and change control cadence."
      },
      {
        "Skill gap": "Operator or number two recruiting and retention design",
        "Identified by": "self-identified",
        "Description": "They want a strong #2. On Nov 4, Juan said they must design a compensation package so the licensed leader (e.g., master electrician) stays. They need help with role profile, comp, incentives, and stay bonuses to keep that leader in place, including sales leadership if the seller is the VP of sales. On Dec 09, Juan noted that keeping an owner on is an expense that must come from price or structure; he wants guidance on salary vs performance-note options and the SDE/bankability impact."
      },
      {
        "Skill gap": "Owner-led sales and light outbound playbook (if needed)",
        "Identified by": "inferred by system",
        "Description": "They said sales is not their forte (though adaptable). Many SMBs need simple, owner-led BD. A basic outbound and account management playbook will help if the target requires it."
      },
      {
        "Skill gap": "Multi-line complexity and capital project gating",
        "Identified by": "self-identified",
        "Description": "On the trucking deal they said it was “four businesses in one” and it required a $2.1–$2.7M build-out loan they do not want to take. They need a clear pass filter and a short checklist to avoid complex, multi-unit deals and big build-outs for their first acquisition. On Dec 09, Juan reaffirmed he is still leaning no due to roughly $2M CapEx for a gas station/strip mall and the multi-entity setup, though he is open to hear the broker pitch."
      },
      {
        "Skill gap": "Remote-operability assessment for out-of-area targets",
        "Identified by": "inferred by system",
        "Description": "For the glazier/blinds business 2.5 hours away, they want to know how often they must be on site and how strong the #2 is. A simple question list will help them judge daily presence needs and remote fit before advancing."
      },
      {
        "Skill gap": "Broker-facing buyer profile positioning (targeted answers; avoid “industry agnostic”)",
        "Identified by": "inferred by system",
        "Description": "Brokers screen buyers by these forms. They agreed to tailor answers to each specific deal (e.g., name the industry like glass and blinds, mark timeline as ASAP). A template will help keep messaging sharp and consistent."
      },
      {
        "Skill gap": "AI-risk screen for digital/online categories and marketing agencies",
        "Identified by": "self-identified",
        "Description": "On Nov 18, they asked to revisit industries they crossed out due to AI risk and requested examples and category lists. They want a simple framework to spot AI‑resistant models (for example, strategic, retainer-based work in durable niches) and to confirm a strong GM/#2 so they are not “buying a job.”"
      }
    ],
    "Coaching/mentoring receptivity (what works best)": [
      "They asked for a coach and “a sounding board,” and said they want Athena to push their thinking.",
      "They are very open to direct guidance.",
      "They act fast. They finish tasks within 24 hours when given clear next steps (e.g., SBA prequal, document prep).",
      "They prefer structured support: checklists, SOPs, maps, sample scripts, and recorded calls. They loved the diligence tracker and model walkthroughs.",
      "Live, step-by-step works: during the NDA walkthrough they screen-shared, edited titles, and added “business owner” on the spot; they also adopted broker feedback to complete all buyer profile fields going forward.",
      "They ask precise questions and apply feedback quickly (e.g., Live Oak form details, lender contact shift to Wendy, SBA structuring).",
      "They decide with both numbers and gut. Give them a financial model plus a simple “fit test” (mission, lifestyle, risk). They will align on both.",
      "Keep both on the same page. Both must say “yes.” Provide trade-off summaries and short written recaps so they can review together.",
      "Give them practice reps. They will benefit from live broker/owner calls, question lists for each step, and quick debriefs with clear go/no-go criteria.",
      "Point them to office hours for lender/legal questions. They use those sessions and will bring back answers to move faster.",
      "Open to expert help and side-by-side structures. They asked targeted SBA questions (seller rollover PG, 51% rule), are open to private capital if SBA is not ideal, and will use QoE and industry experts when a deal has a learning curve.",
      "Responds well to reframes that reduce fear (e.g., “LOIs benefit the buyer; non-binding”). On Nov 11 this increased their comfort to submit offers quickly.",
      "Values candid broker intel and critical feedback. They invited Ryan to be critical and use that guidance in decisions.",
      "Practices and iterates on deliverables. They rehearsed their intro video multiple times and used it to break through gatekeeping on a hot process."
    ]
  },
  "7) Work Environment Fit": {
    "Preferred work environment": [
      "Remote-first with planned visits: Works best from home office with strong systems and dashboards. Ideal schedule includes weekly or monthly on-site visits for training, team meetings, or field checks. Can handle sites 2-3 hours away if team runs independently after initial ramp-up.",
      "Structured yet flexible: Needs clear processes, SOPs, and defined roles, but wants freedom in execution. Prefers organized tools (Slack threads, dashboards, automated tasks) over constant meetings.",
      "Collaborative and low-ego culture: Values psychological safety, open communication, and honest feedback without blame. Wants kind, professional teams where people support each other.",
      "Autonomous with clear accountability: Works best with outcome ownership, not micromanagement. Needs defined goals, KPI dashboards, and simple weekly check-ins.",
      "Quick response culture: Thrives with fast email/text replies and timely financial updates. Clear deadlines and responsive partners maintain momentum.",
      "Steady pace with occasional sprints: Day-to-day should be calm and predictable. Can handle intense periods for closing, integration, or emergencies, then return to normal rhythm.",
      "Family-friendly schedule: Core hours 8am-5pm Central. Must accommodate daycare pickup at 3pm when needed. Protected family time on Friday afternoons.",
      "Mix of desk and field work: Juan enjoys both spreadsheet analysis and hands-on field work with crews. Bilingual environments are ideal.",
      "Data-driven with room for judgment: Wants clean reports and time to think before deciding. Comfortable with 70-80% certainty when speed matters, as long as safeguards exist.",
      "Tolerance and boundaries — Will work intensely during first 90-180 days and true emergencies, but needs defined endpoints and return to normal pace",
      "Tolerance and boundaries — Even during busy periods, requires clear priorities and planned stopping times",
      "Tolerance and boundaries — Needs protected focus time - avoid back-to-back meetings or stacked deadlines",
      "Tolerance and boundaries — For major decisions like LOIs, prefers next-day review unless timeline demands immediate action",
      "Tolerance and boundaries — Can decide with 70-80% of information when needed, but requires clear guardrails and follow-up verification"
    ],
    "Work environments to avoid": [
      "Constant crisis mode: Daily urgency, competitor battles, or always-on culture leads to burnout (especially for Mollie).",
      "Night and weekend heavy: Regular late nights or weekend work conflicts with family priorities. Short planned periods okay, not as lifestyle.",
      "Rigid bureaucracy: Mandatory office attendance, excessive meetings, and process-heavy environments drain energy.",
      "Chaotic operations: No SOPs, unclear roles, or crisis-driven leadership creates stress.",
      "Complex multi-business operations: Juggling unrelated business units (like trucking + retail + fuel + real estate) feels overwhelming for first acquisition.",
      "Heavy regulatory burden: Constant compliance audits or owner-required licensing that dominates daily work.",
      "Toxic culture: Gossip, disrespect, or fear-based management are dealbreakers.",
      "Heavy cold-calling requirements: Boiler-room sales or aggressive new customer hunting doesn't fit their style.",
      "No growth potential: Stagnant businesses with no improvement path will disengage Juan over time.",
      "Daily long commutes: Required daily travel to sites 2-3 hours away won't work with family needs.",
      "Solo operations: Businesses with no existing team where they must build everything from scratch."
    ]
  },
  "8) Deal Experience (evolving)": {
    "Table": [
      {
        "Deal Name": "3-Laundromat Package (DFW, Facebook lead)",
        "Date of Last Update": "Sep 05, 2025",
        "Current Status / Notes": "Spoke with seller, toured sites, built P&L and model. Seller wanted about 6–7x SDE. Self‑serve model, doors controlled by phone, one 1099 cleaner. Seller claimed about $26k/month net. Juan negotiated but could not get price to a bankable level, so they walked."
      },
      {
        "Deal Name": "4-Cabin STR Portfolio (SE Oklahoma, \"LRC\")",
        "Date of Last Update": "Sep 12, 2025",
        "Current Status / Notes": "Closed May 2024 on 26‑acre, 4‑cabin riverfront property with 100% seller financing and 20% down. Acted fast: first meeting same day, site visit next day, offer within a week. Post‑close improvements: added revenue‑management software, hot tub, observation deck, rebrand and new website in progress. Faced early issues: AC failure night one, well‑water capacity during hot tub fill, cleaner and handyman turnover. Still operating and optimizing; plan to hold, improve, then consider sale within 1–5 years."
      },
      {
        "Deal Name": "House Roofing and Restoration (Rockwall, DFW)",
        "Date of Last Update": "Oct 23, 2025",
        "Current Status / Notes": "Passed. First AcquiMatch write‑up reviewed; they liked broker (Toby) and seller (Justin), and seller was open to stay on in a commission‑based sales/#2 role. They chose to pass because net after debt would be well below their income target (no‑growth take‑home estimated ~$160k if paying the seller), and the one‑man model would require building the whole team. They informed broker/seller the next morning to keep goodwill."
      },
      {
        "Deal Name": "DFW Glazier and Blind Manufacturer (Ben Wheeler, TX)",
        "Date of Last Update": "Dec 04, 2025",
        "Current Status / Notes": "Sale paused by broker until 2026. Earlier delays on clean YTD/TTM lowered trust. Will revisit if/when re‑listed; real estate in play; may bring in QoE if they advance."
      },
      {
        "Deal Name": "Trucking and Diesel Services (Frisco area)",
        "Date of Last Update": "Dec 09, 2025",
        "Current Status / Notes": "Reconsideration possible. Originally passed due to multi‑line complexity and ~$2.1M capex tied to a strip‑mall/gas station build. Broker now says owner wants to stay on post‑close; SDE ~$1.2M and price/structure may be flexible. Juan and Mollie are still leaning no but are open to a broker call; they requested 2025 figures to check trend. Any owner salary would need to come from price or a performance‑note structure; they will not take another build‑out loan."
      },
      {
        "Deal Name": "Electrical Services Company (DFW)",
        "Date of Last Update": "Nov 24, 2025",
        "Current Status / Notes": "LOI submitted and then revised to anchor to 2025 projections; included a short intro video that drew positive feedback from brokerage leadership. Not selected to advance; broker reported IOIs ranged ~4.75–6.5x. Moving on. Earlier key diligence: verify personal‑expense ad backs (QoE), ~40–45% top‑3 referral‑channel concentration, day‑1 license coverage (retain/hire master electrician), and a strong non‑compete given seller’s new‑construction plans."
      }
    ],
    "What went well": [
      "Made fast, firm decisions on complex deals (passed on trucking to protect focus and capital)",
      "Successfully tailored buyer profiles to each specific deal instead of using generic \"industry agnostic\" language",
      "Developed quick marketing assessment test - clear ideas for blinds opportunity, none for trucking",
      "Maintained professional relationships with brokers/sellers when passing on deals",
      "Submitted first LOI quickly with creative intro video that got positive broker feedback",
      "Identified key risks early (non-compete needs, license holder dependencies, referral concentration)"
    ],
    "Challenges / freeze points": [
      "Multi-business complexity and large capital requirements block progress on otherwise interesting deals",
      "Struggled when marketing path isn't immediately clear - this became a key decision filter",
      "Uncertain financial categorizations and ad backs create hesitation until verified",
      "Licensed trade dependencies require clear retention/hiring plans before proceeding",
      "Slow broker/seller responses on financials reduce trust and momentum",
      "Limited deal flow under original industry parameters led to scope expansion",
      "Uncertainty about competitive pricing ranges (electrical deal had wide 4.75-6.5x spread)",
      "Questions about whether low buyer interest signals hidden problems"
    ],
    "Learning curve": [
      "First deals should be focused single businesses, not complex multi-unit operations",
      "Marketing clarity test now applied early - if they can't see practical levers, they pass",
      "Maintain price discipline and avoid new development loans at closing",
      "Verify financials early and prepare for Quality of Earnings when numbers seem off",
      "Use LOIs strategically to open books on competitive deals, then verify with lenders",
      "License holder plans must be firm conditions in LOI/purchase agreement",
      "Broker/seller responsiveness indicates readiness - delays are warning signs",
      "Can make 70-80% confident decisions pre-LOI when timelines demand speed",
      "Short intro videos help break through broker gatekeeping in competitive situations",
      "Expanded search to include select digital categories with strict AI-resistance criteria",
      "Owner retention requires modeling salary impact on deal economics"
    ],
    "Notes from transcripts/interactions": [
      "Oct 28, 2025: Glazier deal - waiting over a week for financials, location 2.5 hours away, questioning daily presence needs",
      "Nov 04, 2025: Electrical deal - verified large personal expense add-backs would need QoE, flagged 40-45% concentration risk, planning master electrician retention",
      "Nov 11, 2025: Submitted first LOI based on projections without full TTM data, practicing faster decision-making with partial information",
      "Nov 18, 2025: Expanded industry scope to include MSPs, cybersecurity, ISPs, and related tech services while maintaining SDE/DFW requirements",
      "Dec 09, 2025: Trucking reconsideration - any owner staying must be paid through price/structure adjustment, not additional salary burden"
    ]
  },
  "9) Personal & Family Context": {
    "Spouse/partner (name if shared, profession if relevant)": [
      "Mollie Vidri — Creative and Optimization Strategy Lead at Square (payments/marketing).",
      "Juan Vidri — Senior Product Marketing Manager at eBay (payments/credit cards)."
    ],
    "Role in Decisions": [
      "Role in Decisions: Co-equal. Active in diligence, seller calls, and integration planning. Either partner can veto. Both must say yes.",
      "Role in Decisions: Co-equal. Active in diligence, modeling, negotiation, and financing structure. Either partner can veto. Both must say yes."
    ],
    "Children/dependents (ages if relevant)": [
      "Two young children, 15 months apart. As of Nov 2025: son turns 3 on Nov 9, 2025; daughter (Cleo) is about 20 months old. Both attend daycare 8 a.m. to 5 p.m. (center hours 7 a.m. to 6 p.m., flexible).",
      "Pet: Jack, a 3‑year‑old lab.",
      "Family support: Mollie’s parents live about 30 minutes west toward Weatherford. In Nov 2025, Juan’s sister flew in from El Salvador to help with the kids during Mollie’s work travel; extended family support is available when needed.",
      "Family event: Juan’s mother passed in February 2025; he traveled to El Salvador to be with her and took about a month off work with full support from his employer."
    ],
    "Key dates (birthdays, anniversaries) for relationship/scheduling": [
      "Son’s birthday: November 9 (turned 3 in 2025).",
      "Not shared yet: birthdays for Mollie, Juan, and their daughter.",
      "Not shared yet: wedding anniversary date.",
      "Please collect and add dates so we can plan outreach around them."
    ],
    "Lifestyle priorities: hours, travel, relocation boundaries": [
      "Work hours",
      "First 90–180 days: will operate the business full time with hands-on leadership to learn and stabilize.",
      "After stabilization: do not want to “buy a job.” Target a manager‑led cadence.",
      "Family rhythm: daycare drop‑off around 8 a.m.; prefer to pick up by 3–5 p.m. Avoid routine night work. Friday afternoons are often family time.",
      "Travel",
      "Light, planned travel is fine. Each may have occasional work trips. They can still make meetings while traveling.",
      "Family values personal travel and would like the freedom to take trips.",
      "Recent travel: Traveled to El Salvador for Thanksgiving week 2025. Christmas 2025: staying local with Mollie’s parents; no travel planned.",
      "Home base and relocation",
      "Home: Fort Worth, Texas (Aledo/Fort Worth border), Central Time.",
      "DFW‑first search. Open to hybrid or remote‑operable businesses.",
      "Prefer to stay in their current Aledo/Fort Worth home; they bought their house about 1.5 years ago. Relocating within DFW (closer to Dallas) would be a last resort, but they would do it for the right business.",
      "Ideal: find a business in Aledo or Hudson Oaks. Open to relocate for a standout opportunity; Florida has been mentioned as attractive, yet relocation remains a “maybe.”",
      "Work setup",
      "Both work from dedicated home offices. Remote‑first, with planned on‑site days as needed.",
      "Juan is comfortable in the field and speaks Spanish. Mollie prefers remote or hybrid with regular team touchpoints."
    ],
    "Motivation (“why”) & long-term vision": [
      "Time and presence with their young children. Control of schedule. Healthier pace than large tech roles.",
      "Purposeful work that helps people and strengthens a team. They want a business that feels meaningful, not just profit.",
      "Autonomy. They want effort to tie to outcomes, not fixed W‑2 pay.",
      "Buy, learn, and grow a steady business with clear levers: digitizing, pricing, CRM, brand, and add‑on services.",
      "Keep or build a strong number two. Move toward a manager‑led model so daily owner hours come down.",
      "Consider roll‑ups if the model fits. Open to selling after growth at a higher multiple.",
      "Likely to pursue more than one business over time. They do a “big move” every 1–2 years and see a portfolio path.",
      "Decision rhythm and family dynamics that shape timing",
      "They decide with both numbers and gut. Typical flow: quick model, site visit or owner talk, then a joint go or no‑go.",
      "They move fast once aligned. Expect 24‑hour responses when deals look real.",
      "Juan will contact experts and lenders to fill gaps. Mollie focuses on people, customer experience, brand, and operations.",
      "They protect family time. Plan around daycare windows and avoid stacking late‑night work except for true sprints.",
      "Notes for the team",
      "Avoid high‑pressure, “fire drill” environments as a steady state. Short sprints are fine; chronic urgency is not.",
      "DFW availability is strong; please schedule key sessions within 8 a.m. to 5 p.m. Central when possible.",
      "Missing items to collect: birthdays and anniversary dates; any school calendar constraints; preferred travel blackout weeks.",
      "Holiday plans: Christmas 2025 — staying local with Mollie’s parents; no travel planned."
    ]
  },
  "10) Interests & Influences": {
    "Hobbies & personal interests": [
      "Mollie",
      "Wellness and personal growth. She enjoys guided meditation, breathwork, yoga, and Pilates. She uses the Insight Timer app for daily or short meditations.",
      "Energy and mindfulness work. She tried a quantum healing session and likes sound baths and practices that help with calm and focus.",
      "Creative and home curation. She loves creating a “vibe” in spaces, from scent to lighting and decor, and leads branding and rebrand work.",
      "Team and people experiences. She enjoys team bonding events and thoughtful group time.",
      "Family time. Evenings with the kids, calm routines, and flexible afternoons when possible.",
      "Juan",
      "Sports and fitness. He follows soccer, UFC, and Formula One, and he lifts weights and runs.",
      "Reading and learning. He likes business books and reads about investing and the tax code to optimize savings and growth.",
      "Meditation. He used to meditate every morning and wants to get back to it.",
      "Negotiation and numbers. He enjoys negotiating, modeling deals, and diving into spreadsheets.",
      "Family and cooking. He cooks lunch or dinner at home and builds his day around time with the kids.",
      "AI tools and automation. He uses ChatGPT in meetings for prep and brainstorming and likes simple automation ideas (e.g., bots to handle repeat tasks)."
    ],
    "Books / thought leaders referenced": [
      "Buy Then Build by Walker Deibel (Juan read this).",
      "An HBR book on buying small businesses (title not specified by the client; Juan is reading it).",
      "egal and deal education they watched:",
      "Barlow & Williams session on SBA structures and standby seller notes.",
      "Stonehenge (Matt) session on private capital options that combine debt and minority equity.",
      "Program content and expert videos they followed:",
      "Athena’s videos and Buyers Club sessions.",
      "Live Oak Bank office hours with Wendy and team."
    ],
    "Podcasts / media influences": [
      "Acquiring Minds podcast by Will Smith (they have listened to many episodes).",
      "They mentioned possibly hearing a related mindset study on Diary of a CEO, but this was not confirmed."
    ],
    "Travel & leisure habits": [
      "Nature getaways and “glamping.” They own Little River Cabins in southeast Oklahoma and enjoy the river, quiet nature, and upgrades like the new deck and hot tub.",
      "Pool Fridays and family days. They often plan light afternoons on Fridays to spend time together.",
      "Travel plans and interests. They want more freedom to take trips. They like Texas and are drawn to Florida and California for future time. They talked about visiting Portugal to see Charis. They prefer glamping over camping. Recent travel: spent Thanksgiving week in El Salvador visiting Juan’s family. Christmas 2025: staying local with Mollie’s parents.",
      "Past moves and home base. They lived in Seattle for a year but returned to Fort Worth to be near family and for a better lifestyle."
    ],
    "Community / social involvement": [
      "They attended TABB (Texas Association of Business Brokers) and have attended Live Oak office hours; they have attended Buyers Club sessions (Athena gave Juan a shout-out). They have not mentioned any ongoing community, volunteer, or group memberships outside of work-related forums.",
      "Contrarian Thinking by Cody Sanchez (they reviewed and decided not to join).",
      "Acquisition Lab (they spoke with them during evaluation)."
    ]
  },
  "11) Psychology & Coaching Insights": {
    "Decision-making style": [
      "Pace: Fast. They want a 24-hour turnaround on real deals. They move from model to site visit to decision quickly. Mollie prefers a next-day review before sending an LOI and will slow same-day pushes when needed.",
      "Process: They decide with both numbers and gut. Juan builds the model and calls experts. Mollie tests the people fit, team, and customer feel. She also runs a quick “marketing fit” test: if they cannot see a few simple, practical marketing levers to pull, they will pause or pass.",
      "Ownership: Both must say yes. Either partner can veto.",
      "What to give them: A few strong options, not a long list. Share plain pros and cons, risks, DSCR, and cash after debt. Include a simple “fit test” (mission, time load, risk). Add an effort-versus-payoff view, the team-build load, and net after paying a seller-as-#2 if relevant. Include a one-liner on the top 3–5 marketing moves they could make; lack of clear levers is a red flag for them.",
      "Effort vs payoff filter: If the same effort on a bigger deal will meet or beat their income bar, they will pass on the smaller deal even if the people fit is strong. They will send a clear, respectful pass quickly to keep goodwill with brokers and sellers.",
      "Practice reviews: They will review smaller-SDE deals to get reps and look for a hidden gem, but they will keep their income bar firm for any deal they would buy.",
      "Hot-process approach: On fast-moving deals, after a broker call (with both on the line) and a basic model, they are willing to submit an LOI to open the books and then validate with lenders before paying for a QoE. They are comfortable making decisions with 70–80% of the data pre‑LOI when timelines are short, then verifying with lender screens and QoE.",
      "Levers for flexibility: Size (SDE) is firm. They will first expand industry options to increase deal flow. If that is not enough, they may open geography later; they prefer to keep DFW-first for now.",
      "Broker relationships and signals: Even when leaning no, they will take a broker call to keep the door open and learn. Before re-engaging a passed deal, they ask for current-year trend data (for example, 2025 figures) and want to know why buyer interest is low."
    ],
    "Motivators": [
      "Freedom and family: Control of schedule, time with their two kids, no more corporate grind.",
      "Purpose: Work that helps people and builds a happy team. They want meaning, not just profit.",
      "Growth: Buy, improve, and scale. They like steady growth, roll-up potential, and raising the multiple. They will “go bigger” when returns justify it and the effort is similar.",
      "Security: Healthy cash flow, DSCR near 2.0, and clean structure matter to them.",
      "Knowledge transfer: They value sellers who will stay on as a #2/GM or sales lead to speed ramp and protect relationships.",
      "Action and learning: They enjoy deal-making and like moving fast; taking action and learning by doing is energizing."
    ],
    "Fears / sensitivities": [
      "Buying a job or a burnout role.",
      "AI risk. They want to avoid tech/online models that can be copied or crushed.",
      "Overpaying. Multiples above 4x without strong reasons. Weak DSCR.",
      "Hidden costs and weak working capital. Vendor churn after close.",
      "Heavy regulation or long-path owner licensing that traps them.",
      "Toxic culture, high-pressure “fire drill” markets, or heavy cold-calling sales.",
      "Younger sellers who might compete post-close; want a strong non-compete or the seller to stay on in a sales role. Extra sensitive if the seller is starting a related new-construction company.",
      "Small deals that soak the same effort but miss their income bar; one-person shops that require building the whole team from scratch.",
      "Complex, multi-line deals that feel like several businesses in one for a first acquisition.",
      "Big build-outs tied to the deal or right after close, especially if they require taking another loan to fund development.",
      "Unclear marketing path where they cannot see practical, simple levers to pull.",
      "Slow or disorganized sellers/brokers and delayed YTD/TTM updates; these lower trust and interest.",
      "Marketing agency without a strong GM/lead (would feel like “buying a job” for Mollie).",
      "Low buyer competition on a seemingly strong deal; Juan sees this as a possible red flag and wants to understand why interest is low."
    ],
    "Stress triggers": [
      "Constant urgency or a competitor “breathing down their neck.”",
      "Stacked late nights, back-to-back travel weeks, or too many meetings.",
      "Unclear steps, messy data, or slow broker/lender responses, including vague timelines and fuzzy ad backs/backlog definitions.",
      "Surprise failures or vendor gaps (they lived this in the cabins: AC failure night one, water capacity, cleaner change).",
      "Pressure to send a same-day LOI without a short review step.",
      "Being asked to juggle several business lines at once (e.g., operations plus new retail, fuel, and real estate).",
      "Requests for large capital injections or extra loans to fund build-outs as part of the deal.",
      "A deal where they cannot see straightforward marketing moves.",
      "Hard daycare pickup windows; last-minute overruns near pickup time.",
      "Waiting with no updates after sending an LOI; the idle period is uncomfortable.",
      "Ambiguous broker emails with no clear yes/no; Juan tends to reread and overthink wording during waits."
    ],
    "Coping style": [
      "They slow down by modeling, checklists, and a pros/cons list. Then they talk it out together.",
      "Juan calls experts and office hours to fill gaps. Mollie centers on people, plan, and customer impact.",
      "Short resets help (gym, quick meditation, family time). They like clear routines.",
      "They use AI tools (e.g., ChatGPT) during prep and in meetings to brainstorm and organize fast.",
      "They apply an effort-versus-payoff check and, when needed, send a quick, respectful pass to preserve goodwill.",
      "Mollie runs a quick “marketing fit” check. If ideas are thin, they step back and reassess.",
      "On hot processes, they use an LOI to open the books and let lenders act as an early QoE check before paying for a full QoE. They set clear conditions in the LOI (e.g., license-holder retention/hire, non-compete) to manage risk.",
      "A simple mantra helps: “LOIs benefit the buyer and are non‑binding.” This reduces fear and supports fast but controlled action with 70–80% of the data.",
      "During waiting periods, a simple update cadence and small tasks (like reviewing category lists) help channel energy."
    ],
    "Preferred communication": [
      "Direct, structured, and warm. Big picture first, then key numbers.",
      "Give checklists, SOPs, and 1-2-3 next steps with deadlines.",
      "Provide short written recaps they can review together, plus a trade-off table.",
      "Record broker calls and share links. Use one shared Slack thread.",
      "For each LOI, include a one-page summary: price, structure, DSCR, working capital plan, key risks, and day-1 focus.",
      "Protect mental clarity: avoid back-to-back stacks; late afternoon windows (e.g., after Buyers Club) work well. If passing, a short, kind template they can send the same or next morning helps maintain relationships.",
      "For broker forms, provide targeted wording they can use (name the specific industry rather than “industry agnostic,” mark timing as ASAP).",
      "On hot deals, set a clear end-of-week target, remind them that an LOI advantages the buyer by opening the books, and schedule the broker call with both present.",
      "Share candid broker intel and simple gatekeeping workarounds (for example, a short intro video) to get attention in competitive processes.",
      "Async lists or screenshots are fine; they review at night after the kids are asleep and while traveling.",
      "When revisiting a passed deal, include the latest-year figures (e.g., 2025 trend) and a simple note on owner-stay pay coverage (price reduction vs performance note) so they can judge SDE and DSCR impact fast."
    ],
    "Development areas": [
      "Deal discipline: They can get excited by many businesses. Keep them “sniper,” not “shotgun.” Hold the line on industry NOs, multiples, DSCR, and time-load.",
      "Diligence depth: Mollie wants help with what to ask and how to spot red flags. Give question lists for CIM, financials, customer mix, vendor depth, and key staff. Include an ad back/QoE trigger checklist.",
      "Finance comfort for Mollie: Build her confidence with P&L tie-outs, ad backs, DSCR, and cash flow views. Use simple dashboards and plain language.",
      "Working capital and cash cycles: Juan asked for strong support here (including seasonality). Size buffers so they avoid a crunch.",
      "Structure guidance: Juan wants clarity on SBA rules, seller notes on standby counting as equity, HELOC and PG strategy, and private capital options (e.g., Stonehenge). Also clarify seller rollover equity rules (does a seller keeping ~10% need to PG? 51% control requirement). Provide a simple decision tree.",
      "Pause-to-plan for Juan: He knows he used to act before planning. Give pre-mortems, checklists, and a “cooling step” before LOIs to keep him thoughtful.",
      "Licensing and compliance map: They are open to HVAC/electrical. They need clear timelines and options when a licensed leader is required.",
      "100-day plan and change control: They want to “learn and maintain” first. Give a 30/60/90 plan with a short change freeze and a cadence for small, safe wins.",
      "Operator / #2 plan: Help define the role profile, comp, incentives, and retention so the day-to-day becomes manager-led. Include SDE impact if the seller stays on as a #2/GM or VP Sales. If the owner stays, compare salary vs a performance-note mix and show the DSCR and bankability impact.",
      "Simple owner-led sales playbook: If needed, give a light BD plan (top accounts, warm outreach rhythm, quoting rules) that does not require heavy cold-calling.",
      "Burnout guardrails for Mollie: She tends to take on too much. Set clear split of duties, delegation plans, and weekly stop-times during search and integration.",
      "Deal size confidence and risk framing: Bigger deals feel scary even when they fit. Provide a short “why this is okay” case (DSCR, cash buffer, team plan) to support go/no-go.",
      "Complexity and capital projects: Build a clear pass filter for multi-line, “several businesses in one” deals and for any deal that needs large build-outs or extra loans at or right after close.",
      "Early marketing-fit screen: Add 3–5 simple marketing levers to each brief. If none are obvious, flag as likely not a fit.",
      "Broker-facing positioning: Give them a short buyer-profile template to tailor per deal; avoid “industry agnostic” and set timing to ASAP.",
      "Pre-LOI pacing on hot deals: Coach them to use an LOI to open the books after a broker call and basic model, then run lender checks before paying for QoE.",
      "License-holder condition in LOI/APA: For licensed trades, make retention or hiring of the master license holder a clear condition, and design a stay/comp plan to keep that leader in seat.",
      "Decision-making with 70–80% information pre‑LOI: Provide a short checklist and guardrails so they can move fast while managing risk.",
      "Seller readiness and trust signals: Add a quick screen for responsiveness and clean YTD/TTM; slow or messy updates are a warning sign to pause or de‑prioritize.",
      "AI-risk screen for digital/online categories and marketing agencies: On Nov 18 they asked to revisit some “no” categories. Provide a simple test (strategic, retainer-based work in durable niches; clear GM/#2 so they are not buying a job) and add it to briefs.",
      "Manage overanalysis during waiting periods: Set a simple post‑LOI update cadence and discourage reading between the lines of broker emails; give small tasks to focus on while waiting.",
      "Buyer-pool signals and competition: Help them read low competition or limited PE interest by industry so they can decide if it is normal or a red flag on a specific deal."
    ]
  },
  "11A) Behavioral Snapshot": [
    {
      "Signal": "Moves fast when next steps are clear; acts within 24 hours",
      "Confidence level": "High",
      "Coaching moves that work": [
        "Give 1–3 clear actions with deadlines; confirm next steps on the call; keep momentum with quick check-ins."
      ],
      "Watch-outs": [
        "Too many options or vague asks can slow them; rapid pace without a short review step can miss details."
      ],
      "Recent examples": [
        "2025-09-05 — “You’ll hear from us in the next 24 hours. We move quick.” What it means: They commit to fast follow-through when the task is clear.",
        "2025-09-05 — On Live Oak prequal: “I can do that tomorrow… it’s almost done.” What it means: They finish paperwork quickly if told what to do.",
        "2025-08-19 — “We’re eager… we’re always going to choose the earliest date.” What it means: They prefer the earliest possible slot and quick starts.",
        "2025-09-23 — “Just met with Wendy and we got the pre-approval letter.” What it means: They moved through lender steps quickly and closed the loop the same day.",
        "2025-10-20 — Transworld NDA: “Will fill it out now” … “please see attached.” What it means: They execute NDAs immediately to keep things moving.",
        "2025-11-10 — “ok updated - just sent over the new LOI based on the 1.1MM projected at 4X.” What it means: They iterate offers same day when new data arrives.",
        "2025-11-11 — “We love to move fast… we prefer that over a longer period.” First LOI submitted and quickly iterated. What it means: They keep speed on hot processes and act fast when timelines are short.",
        "2025-11-18 — “We’ll look through those after the kids go to bed tonight.” What it means: They act on clear tasks the same day, even with family duties.",
        "2025-11-18 — “We have our computers with us… we’ll review at night when the kids are asleep.” What it means: While traveling, they keep momentum with async work."
      ]
    },
    {
      "Signal": "Decides with numbers and gut; runs scenarios; walks if the math fails",
      "Confidence level": "High",
      "Coaching moves that work": [
        "Lead with DSCR, price, and cash after debt; include a simple “fit test” (time load, purpose, risk); keep to ≤4x unless clearly justified."
      ],
      "Watch-outs": [
        "Strong stories can pull attention; keep working-capital, seasonality, and customer concentration front and center."
      ],
      "Recent examples": [
        "2025-09-12 — LRC deal: “For probably 48 to 72 hours, I didn’t sleep… all I did was… my models.” Offer within one week. What it means: They model hard before moving and then act fast.",
        "2025-09-05 — Laundromat: “He wanted 6X, 7X SDE… you know what? It’s not for me… So we walked away.” What it means: They hold price discipline and will walk.",
        "2025-09-05 — “As much as we can, have that DSCR closer to two… I don’t want to go above a 4X multiple.” What it means: Clear guardrails guide decisions.",
        "2025-10-14 — Juan: “That probably signals there’s some hair… explore what’s behind that [low] multiple.” What it means: He wants to understand the risk before moving.",
        "2025-10-23 — Roofing (Rockwall): “The take-home was going to be 160… and we would have had to build an entire team… the amount of effort we would put into here could also be put into a bigger company.” What it means: They favor returns and guardrails over a good people fit.",
        "2025-10-28 — Trucking/Diesel: “Definite pass… four businesses in one… he needs about $2.7M for build-out and asked for roughly a $2.1M injection… we don’t want another loan.” What it means: They avoid complex, capital-heavy deals to protect DSCR and focus.",
        "2025-11-04 — Juan screen-shared the P&L and questioned precise add backs (e.g., house cleaning, lawn, “member annual meeting” ~$42k), the 2023→2024 revenue dip, margins, and top-3 concentration. What it means: He digs into ad backs and trends before deciding and plans QoE to verify.",
        "2025-11-11 — “We don’t have TTM, but we made it based on projections… I need to get comfortable making decisions with 70–80% of the info.” What it means: He will decide pre‑LOI with partial data when timing requires it and verify later.",
        "2025-11-18 — “The threshold for SDE… we probably don’t have much flexibility… I’d rather… take a little bit more time and find a bigger one than… compromise.” What it means: Size and cash flow guardrails are firm and guide choices.",
        "2025-12-09 — “Did the broker share 2025? If it’s trending even more in 2025, that would… make it even more appealing.” What it means: He asks for current-year trend data before re‑engaging a passed deal.",
        "2025-12-09 — “Is [low PE interest] a red flag?” (re: $1.2M SDE trucking/logistics). What it means: He probes buyer‑pool signals to sense hidden risks before advancing."
      ]
    },
    {
      "Signal": "Comfortable in seller talks and negotiation; enjoys the process but will walk away",
      "Confidence level": "High",
      "Coaching moves that work": [
        "Let Juan lead first-pass negotiations; prep anchors, trade-offs, and talk tracks; debrief fast after each seller/broker call."
      ],
      "Watch-outs": [
        "Keep goodwill with sellers; pair firmness with clarity on structure and path to close."
      ],
      "Recent examples": [
        "2025-09-05 — Juan: “I enjoy the negotiation part… brings me joy… influence people.” What it means: He leans into negotiation moments.",
        "2025-09-05 — Laundromat: Modeled, tried to negotiate, then walked at 6–7x SDE. What it means: He won’t chase bad pricing."
      ]
    },
    {
      "Signal": "Very coachable; asks precise, technical questions and uses resources",
      "Confidence level": "High",
      "Coaching moves that work": [
        "Provide SOPs, checklists, question lists; push their thinking; route lender/legal questions to Buyers Club/office hours; connect them to named contacts (e.g., Wendy)."
      ],
      "Watch-outs": [
        "Avoid unstructured brain dumps; present information in clear steps; don’t overload with 10+ options at once."
      ],
      "Recent examples": [
        "2025-09-05 — “I was going to use this call to ask you… do I attach [the full list]?” (Live Oak PFS detail). What it means: They ask exact how-to questions to do it right.",
        "2025-09-05 — “I would rather work with someone that you guys already work with… Wendy.” What it means: They adopt guidance fast.",
        "2025-08-12 — “I want a coach, a sounding board… Athena pushes people… I think I need that.” What it means: They invite direct coaching.",
        "2025-09-12 — “We live in spreadsheets and SOPs. This is music to our ears.” What it means: Structure increases their speed and confidence.",
        "2025-08-27 — “I think I’ve watched like 10 hours of videos already.” Also asked for anonymized P&Ls to practice. What it means: They self-train fast and request resources to get better.",
        "2025-10-14 — Completed the NDA live on the call, screen-shared edits, and added “business owner” on the title per advice; agreed to fill all buyer profile fields going forward. What it means: They adopt guidance in real time and follow process.",
        "2025-10-14 — Juan: “Probably every meeting I’ve had today, I’ve used ChatGPT… in the meeting, I was brainstorming with it.” What it means: They use tools to move faster and organize ideas.",
        "2025-10-23 — Glazier/Blinds: “You saw how I redlined the entire model… there are a lot of sketchy things… Who spends $16,000 on personal cell phones? $25,000 a year in gas?” What it means: He digs into ad backs and pushes for clear answers.",
        "2025-10-28 — Buyer profiles: Agreed to tailor forms (avoid “industry agnostic,” mark timing “ASAP”) after Charis’s tip. What it means: They adopt positioning guidance to improve broker response.",
        "2025-11-04 — After hearing that LOIs open the books and lenders act as an early QoE check, Juan: “Thank you for saying that… I’ll set up the broker call ASAP… I’ve read the LOI template… I’ll have it ready.” What it means: He adopts pacing guidance on a hot deal and moves fast.",
        "2025-11-07 — “just sent it to B&W.” (LOI to Barlow & Williams for review.) What it means: They use legal experts promptly to shore up offers.",
        "2025-11-11 — “We appreciate you being critical, and please continue.” “We practiced [the video] like five times.” What it means: They invite candid feedback and rehearse deliverables to break through gatekeeping.",
        "2025-11-18 — Reframed AI stance and agreed to test select digital/marketing categories with an AI‑resistant screen; “We’ll look through those after the kids go to bed tonight… We’ll also do research on our side.” What it means: They are open to new frames and take quick, structured next steps."
      ]
    },
    {
      "Signal": "Strong price and risk discipline in financing; probes structure details",
      "Confidence level": "High",
      "Coaching moves that work": [
        "Model DSCR and cash buffer; map SBA rules (standby notes, equity injection), HELOC PG impacts; compare SBA vs private partner in a simple decision tree."
      ],
      "Watch-outs": [
        "Avoid creating lender concerns (e.g., optics of minimizing PG) without aligning on bank view first; keep steps lender-ready."
      ],
      "Recent examples": [
        "2025-09-05 — “As much as we can, have that DSCR closer to two… I don’t want to go above a 4X multiple.” What it means: Clear cash-flow guardrails.",
        "2025-09-05 — “I’m trying to minimize my PG… If I put a HELOC on [the rental]… would Live Oak see it favorable?” What it means: He’s actively shaping structure and risk.",
        "2025-09-05 — “Private equity is not so scary… can increase purchasing power.” What it means: They consider PE-lite alongside SBA.",
        "2025-10-23 — “Can you remind me what the SBA rules are if the seller retains equity? Do they have to PG? What about the 51% control rule?” What it means: He checks SBA rules before choosing a rollover/partnered structure.",
        "2025-10-23 — “I’m on the fence on real estate… we could amortize longer if we buy, or lease it… use a separate real estate entity and have rent flow.” What it means: He wants to model buy vs lease (OpCo/PropCo) and align with lender guidance.",
        "2025-11-04 — “This deal would be contingent on one of these two [candidates] passing and staying… or hire someone else,” and he flagged the seller’s new‑construction company risk to confirm scope. What it means: He sets clear conditions to manage license and potential competition risk.",
        "2025-11-11 — “Quick question… SBA loan limits $5 million vs our $7.75 pre‑approval… is that pari passu?” What it means: He probes lender structures to stay within safe terms.",
        "2025-12-09 — “That’s… an expense to keep him on… we would have to… pay for that,” and noted it must come from price or structure. What it means: He bakes owner‑stay salary into SDE and considers salary vs performance‑note trade‑offs before advancing."
      ]
    },
    {
      "Signal": "Joint, aligned decision-makers; complementary roles; “good cop/bad cop”",
      "Confidence level": "High",
      "Coaching moves that work": [
        "Include both on key calls; share short written recaps they can review together; split diligence roles (numbers/structure to Juan; people/brand/ops to Mollie)."
      ],
      "Watch-outs": [
        "Don’t advance on a partial yes; schedule to fit both when decisions are needed."
      ],
      "Recent examples": [
        "2025-09-05 — “We did it separately, and we had pretty much the same themes.” What it means: They align quickly as a pair.",
        "2025-09-05 — “In every team, you need a good cop and a bad cop.” (They agreed; Juan leads hardball, Mollie covers people/brand.) What it means: Useful dynamic in owner and team conversations."
      ]
    },
    {
      "Signal": "Avoids chronic high-pressure, competitor-driven environments; pressure drains Mollie",
      "Confidence level": "High",
      "Coaching moves that work": [
        "Present plans calmly; avoid “race” framing; set steady cadence with clear roles; timebox sprints; highlight path to manager-led operations."
      ],
      "Watch-outs": [
        "Stacked urgent asks or a “race” narrative can stall decisions or cause anxiety."
      ],
      "Recent examples": [
        "2025-09-12 — Mollie: “I hate pressure… if there’s a competitor… we’ve got to act fast… I would do it, but it drains me.” What it means: Chronic urgency reduces energy and clarity.",
        "2025-09-05 — Amazon story: “5 a.m. to 10 p.m.… not sustainable.” What it means: They’re leaving that lifestyle."
      ]
    },
    {
      "Signal": "Self-awareness about overload and pacing; wants guardrails",
      "Confidence level": "Medium",
      "Coaching moves that work": [
        "Add a pre-LOI “cooling step” and pre-mortem; set weekly stop-times; define delegation plan; keep a one-page go/no-go checklist."
      ],
      "Watch-outs": [
        "Mollie can take on too much and burn out; Juan can act before fully planning if a pause isn’t built in."
      ],
      "Recent examples": [
        "2025-09-05 — Mollie: “I will take on a lot… I get burned out… I’ve improved at delegating.” What it means: Needs planned delegation and boundaries.",
        "2025-09-05 — Juan: “I would jump headfirst… now I take a step back and think and then act.” What it means: A short pause step helps him stay thoughtful.",
        "2025-10-14 — Mollie: “I called Juan to calm down… stop putting your LOIs and let’s have a meeting tomorrow.” Juan: “I need to practice my patience.” What it means: They want a pause step and next-day review before LOIs.",
        "2025-11-04 — Juan: “I need to pick up my kid in three minutes,” then agreed to move the weekly meeting 15 minutes earlier. What it means: Hard daycare pickup windows; protect buffers around end-of-day.",
        "2025-12-09 — “We took the entire week off… didn’t even take our computers.” What it means: They may fully unplug on family holiday travel; plan around this."
      ]
    },
    {
      "Signal": "Broad curiosity can widen the search; asks for focus to avoid “shotgun”",
      "Confidence level": "Medium",
      "Coaching moves that work": [
        "Present 2–3 strong options at a time; force-rank; tie back to the deal box; use a red/green criteria list during debriefs."
      ],
      "Watch-outs": [
        "Too many options at once can create drift or hype; maintain criteria and guardrails."
      ],
      "Recent examples": [
        "2025-09-05 — Mollie: “We can get pretty hyped over any business… we need help finding the right [fit].” What it means: They want external focus to stay disciplined.",
        "2025-09-05 — They embraced “shotgun vs sniper” framing. What it means: They agree to tighter selection.",
        "2025-10-28 — Juan: “I would think no to dropshipping… then I saw 3.7x and $1M EBITDA, remote from Florida… maybe we go in that direction.” What it means: Preferences can shift with facts; keep criteria front and center."
      ]
    },
    {
      "Signal": "Wants to “learn and maintain” first post-close; not buying a job; prefers a strong #2",
      "Confidence level": "High",
      "Coaching moves that work": [
        "Build a 30/60/90 with a short change freeze; plan a few low-risk early wins (pricing, CRM, website); define/operator #2 role, comp, and retention."
      ],
      "Watch-outs": [
        "Don’t push large changes early; be candid about the time load in the first 90–180 days."
      ],
      "Recent examples": [
        "2025-09-05 — “You don’t want to go in there and… tinker too much… You just want to learn and maintain first.” (They agreed.) What it means: Cautious integration is their style.",
        "2025-09-05 — “We don’t want to buy a job.” “Two to four hours [daily] would be ideal later… a good #2 would be great.” What it means: Long-term target is manager-led operations.",
        "2025-10-23 — Roofing: “He could become the number two… but that would eat into our SDE.” What it means: They like seller-as-#2 for knowledge transfer but will not ignore the SDE impact."
      ]
    },
    {
      "Signal": "Embraces 24-hour response expectation on live deals",
      "Confidence level": "Medium",
      "Coaching moves that work": [
        "When sending a vetted deal, set a 24-hour reaction ask; provide a short one-pager; schedule a quick debrief window upfront."
      ],
      "Watch-outs": [
        "None if the ask is clear and materials are concise."
      ],
      "Recent examples": [
        "2025-08-12 — Austin: “If I pass you a deal, we need a 24-hour turnaround.” (They did not object.) What it means: They accept a fast response cadence on real deals.",
        "2025-09-05 — “You’ll hear from us in the next 24 hours.” What it means: They mirror the same standard.",
        "2025-10-14 — First write-up: “We will respond by tomorrow… we will move very fast.” What it means: They kept the 24-hour cadence on a live deal.",
        "2025-10-23 — Roofing pass: “We sent him an email the next day… we didn’t want to hang up anything.” What it means: They close loops quickly and keep goodwill.",
        "2025-11-04 — Electrical deal: Agreed to “sprint to get this LOI… end of week,” and to schedule the broker call when Mollie returns. What it means: Keeps fast cadence on a hot process.",
        "2025-11-11 — “We’ve got first official offer out… now I have to wait, and we hate that.” What it means: They move fast to submit and iterate; idle time after an LOI is uncomfortable.",
        "2025-11-14 — Cash: “you might ping them…” Juan: “Just did.” What it means: They follow up proactively to keep pressure and timelines.",
        "2025-11-18 — Travel week: “We’re traveling on Tuesday… we can’t meet… but we have our computers… we’ll review at night when the kids are asleep.” What it means: They keep a fast response cadence with async work even during travel."
      ]
    },
    {
      "Signal": "Uses a quick “marketing fit” test to guide go/no-go",
      "Confidence level": "Medium",
      "Coaching moves that work": [
        "In each brief, list 3–5 simple marketing levers they could pull; ask Mollie to outline day‑1 moves; if levers are thin, flag early."
      ],
      "Watch-outs": [
        "If they cannot see a clear marketing path, they will stall or pass; do not force a fit."
      ],
      "Recent examples": [
        "2025-10-28 — Mollie: “Trucking… I wouldn’t even know where to start with marketing,” versus “blinds… a million ideas.” What it means: Clear marketing levers raise confidence to advance; unclear levers are a red flag."
      ]
    },
    {
      "Signal": "Rates seller/broker responsiveness as a trust signal; de‑prioritizes slow or disorganized processes",
      "Confidence level": "Medium",
      "Coaching moves that work": [
        "Ask early for updated YTD/TTM; keep pinging when numbers lag; push for a broker/owner call to test fit; log responsiveness as part of the go‑no‑go."
      ],
      "Watch-outs": [
        "Don’t fully write off a deal only due to slow accounting; an owner call can reset views; keep it warm while waiting on clean numbers."
      ],
      "Recent examples": [
        "2025-11-11 — “This LOI process… made the [blinds] one less attractive because they are slow. We were not getting the numbers in time… they seem to be not ready or disorganized.” What it means: Responsiveness and clean updates shape their confidence and pace.",
        "2025-11-18 — On a vague broker update: “I reread that like 10 times… might be me overanalyzing,” inferring next‑round meetings. What it means: Ambiguous emails during waits increase anxiety; clear timing and updates help."
      ]
    },
    {
      "Signal": "Keeps broker doors open even when leaning no; takes calls to learn and maintain goodwill",
      "Confidence level": "Medium",
      "Coaching moves that work": [
        "Timebox broker calls; ask for the latest-year figures before the call (e.g., 2025 trend); set clear pass criteria and confirm next steps; thank them and keep the door open."
      ],
      "Watch-outs": [
        "Don’t get pulled back into misfit, complex deals; protect capex and complexity guardrails; avoid sunk-time drift."
      ],
      "Recent examples": [
        "2025-12-09 — “I’m still leaning no, but I’m never going to say no to the broker because you never know what other opportunity he or she might have.” What it means: They will still take the call and keep relationships warm even when likely to pass.",
        "2025-12-09 — “Did the broker share 2025? If it’s trending even more in 2025… more appealing.” What it means: They request current-year figures before re‑engaging to judge momentum."
      ]
    }
  ],
  "12) Business Fit Evaluation (simple scoring)": {
    "Leadership match": {
      "Score": "5/5",
      "Notes": [
        "They bring proven leadership skills from managing teams up to 26 people and controlling budgets over $475M. Both have hired, coached, and made tough personnel decisions. Juan connects well with field crews in English and Spanish while Mollie excels at building team culture and communication. They submitted their first LOI quickly with a professional intro video that impressed broker leadership. Their only gap is heavy cold-calling or owner-only sales - they need businesses with existing teams or simple sales playbooks."
      ]
    },
    "Resilience / grit alignment": {
      "Score": "4/5",
      "Notes": [
        "They've handled high-pressure Amazon deadlines and solved day-one cabin emergencies (AC failure, vendor turnover) while keeping guests happy. They move fast on decisions but maintain discipline - walking away from deals that don't meet their financial targets. They'll work intensely during the first 90-180 days and handle true emergencies, but chronic urgency drains them (especially Mollie). They need defined endpoints and a return to steady pace after sprint periods."
      ]
    },
    "Complexity tolerance (ops, compliance, multi-site)": {
      "Score": "3/5",
      "Notes": [
        "They can handle multi-site operations with clear SOPs and teams of 10-40 employees. They'll model real estate decisions and bring in experts for specialized sectors. However, they avoid \"several businesses in one\" deals, heavy regulation requiring owner licensing, and deals needing major capital projects at closing. For licensed trades, they only proceed if a master license holder is secured before closing. Slow or disorganized financial reporting reduces their confidence."
      ]
    },
    "Operational energy (field time, people intensity)": {
      "Score": "4/5",
      "Notes": [
        "They commit to full-time, hands-on leadership initially. Juan enjoys field work with crews while Mollie prefers hybrid setups with planned team touchpoints. Both want to build toward manager-led operations over time. They can handle sites 2-3 hours away if teams are self-sufficient after initial ramp-up. They won't fit businesses requiring 50-60 hour weeks indefinitely or one-person operations needing complete team building from scratch."
      ]
    },
    "Values alignment (legacy, community, employees)": {
      "Score": "5/5",
      "Notes": [
        "They want meaningful work that helps people, not just profit. They respect seller legacies, plan to keep existing staff, and prefer working with retiring owners or younger sellers who'll sign strong non-competes. They value responsive, organized sellers who provide clean financials promptly. They communicate professionally when passing on deals to maintain relationships. Family time and community impact matter deeply - they need businesses that align with their DFW-first, family-friendly schedule."
      ]
    }
  },
  "13) Interaction Notes & Red Flags": {
    "Decision & communication patterns": [
      "Joint decision-making: Both Juan and Mollie must say yes. Either partner can veto. Never advance on partial agreement.",
      "24-hour response time: They commit to fast turnaround on real opportunities and close loops quickly with brokers/sellers.",
      "Numbers plus gut approach: Juan builds financial models while Mollie evaluates team fit and customer experience. Both run a \"marketing clarity test\" - if they can't see 3-5 simple growth levers, they pause or pass.",
      "Structured information preferred: They work best with one-page summaries, checklists, and 2-3 clear options rather than long lists. Include DSCR, cash after debt, and simple \"fit tests\" for mission/lifestyle/risk.",
      "Real-time collaboration: They screen-share during calls, make edits live, and use ChatGPT for brainstorming during meetings.",
      "Next-day LOI review: Mollie prefers pausing before sending LOIs to avoid rushing. On hot deals, they'll submit quickly to open books, using lenders as early quality checks.",
      "Written recaps for alignment: Both partners need short summaries they can review together, especially for major decisions.",
      "Async work during travel: They review materials at night when kids are asleep and can jump on ad-hoc calls. May fully unplug during family holidays.",
      "Broker relationship maintenance: They send professional, timely responses when passing on deals to preserve relationships for future opportunities."
    ],
    "Red flags (biases, blind spots)": [
      "\"Shotgun\" tendency: Can get excited about many businesses at once. Risk of drifting from core criteria without external focus.",
      "Burnout risk for Mollie: Takes on too much and gets drained by high-pressure, urgent environments. Needs delegation plans and protected time.",
      "Speed risk for Juan: Can push for same-day LOIs without adequate review. Needs structured pause points before major commitments.",
      "Working capital blindness: Learned from cabin experience about hidden costs and vendor issues. Risk of underestimating cash needs.",
      "Complex deal attraction: Despite knowing better, can be drawn to multi-business operations that overwhelm first-time buyers.",
      "Marketing path dependency: Will freeze or pass if they can't identify clear, practical marketing opportunities immediately.",
      "License holder uncertainty: Won't proceed without secured master license holders but may underestimate hiring difficulty.",
      "Low sales comfort: Heavy cold-calling or aggressive customer acquisition doesn't fit. Need existing pipeline or simple playbook.",
      "Analysis paralysis during waits: Juan tends to reread vague broker emails multiple times. Idle periods after LOI submission create anxiety.",
      "Geographic compromise risk: May consider deals 2-3 hours away without fully assessing daily presence requirements.",
      "Income bar pressure: Needing $550-600k after debt significantly narrows options and could create timeline stress.",
      "One-person operation trap: Risk of considering solo businesses that require building entire teams despite knowing the effort-payoff mismatch."
    ],
    "Opportunities (where they shine if positioned well)": [
      "Use their \"sniper not shotgun\" framework: Present 2-3 focused options at a time. Force-rank against deal criteria. Keep them disciplined.",
      "Leverage their 24-hour commitment: Set clear deadlines and provide concise briefs to maintain momentum.",
      "Build in pause points: Schedule next-day reviews before LOIs. Add pre-mortem checklists to slow Juan while keeping Mollie engaged.",
      "Split responsibilities clearly: Assign numbers/structure to Juan, people/culture to Mollie. Play to their complementary strengths.",
      "Provide simple frameworks: They love checklists, templates, and step-by-step processes. Give them tools they can apply immediately.",
      "Use recorded content: Share broker call recordings and maintain single Slack threads for deal discussions.",
      "Frame decisions positively: Simple reframes like \"LOIs benefit the buyer\" reduce anxiety and support action.",
      "Create marketing clarity early: Include 3-5 specific growth levers in every brief. No clear levers = early pass signal.",
      "Protect energy systematically: Set weekly stop-times, avoid back-to-back meetings, schedule calls after 4pm CT when possible.",
      "Channel waiting anxiety productively: During LOI waits, assign specific tasks like reviewing new categories or preparing seller questions.",
      "Leverage their professional approach: Their respectful communication with sellers/brokers opens doors others might close.",
      "Use success patterns: They respond well to structured expert resources (office hours, legal reviews) when pointed clearly.",
      "Apply their \"effort vs payoff\" filter: Help them pass quickly on small deals requiring same effort as larger opportunities.",
      "Build confidence through practice: They want to review smaller deals for learning while maintaining their income bar for actual purchases."
    ]
  },
  "14) At-a-Glance (what’s been done / what’s next)": {
    "Current focus (this month)": [
      "No new deals were requested to Mausam’s team in December"
    ],
    "Next up (queued)": [
      "Home services trades with licensed leader (HVAC, electrical)",
      "Remote, tech‑light, manager‑led businesses"
    ],
    "Recently covered (last 2 months)": [
      "Manufacturing"
    ],
    "Hard NOs": [
      "Car Dealerships, RV Dealers, Coolsculpting, Cosmetic & Plastic Surgery, Hair Salons, Nail Salons, Weight Loss, Advertising & Design, Advertising Agency, Digital Marketing, Internet Publishers, Newspapers, Periodicals & Magazine Publishers, Radio Stations, SEO Companies, Television Stations, Web Design & Development, Adoption Agency, Dance Studios, Tutoring, Tutoring Centers, Seminars, Specialized/Career Education, Teachers, Virtual/Online Learning, Vocational Trades Education, Amusement Parks, Antique Dealers, Escape Rooms, Magicians, Nightclubs & Theaters, Psychics, Tattoo Studios, Videography, Accounting & Tax Services, Bookkeeping, Brokerage & Security Dealers, Check Cashing, Collection Agencies, Crypto Related, Factoring, Addiction Treatment Center, Cardiologist, Chiropractors, Counselors, Dental Services, Dermatologists, Dietitians, Doctors, Hearing Aid Store, Hospitals, Hypnotherapists, Laser Eye, Lasik, Massage, Nutritionists, Optical Services, Pediatricians, Physical Therapists, Psychiatrists, Psychologists, Psychotherapists, Rehab, Speech Therapists, Telehealth, Urologists, Vein Clinic, Acupuncture, Clothing & Footwear Manufacturing, Computer & Chip Manufacturing, Content sites (affiliate/advertising), Digital products, Dropshipping, eCommerce/Amazon FBA, KDP businesses, Mobile Apps, SAAS, Web Design & Development (service), Computer Repair, Computer Store, Network Consultants, Point of Sale Systems, Veterinarians, Bakeries, Bars, Breweries, Cafes, Catering Services, Coffeeshops, Cafes & Dessert Shops, Convenience Stores, Food & Beverage, Food & Beverage Distribution & Routes, Food Production & Packaging, Food Trucks, Grocery & Supermarkets, Juice Bar, Liquor & Wine, Liquor Licenses, Mexican Restaurants, Pizzerias, Restaurants, Sandwich Bar, Sushi Restaurants, Takeaway Restaurant, Vegan Restaurants, Vending Machines, Appliance Repair, Bedding Store, Bicycle Store, Bookstores, Boutique, Bridal Shop, Camping Stores, Car Decals, Card & Stationery Stores, Cash for Gold, Childrens Clothing Stores, Clothes Retail, Craft Supplies, Electronics Store, Embroidery Services, Fabric Shops, Fishing Supplies, Flooring, Furniture Stores, Garden Centeres and nurseries, Gift Shops, Gun Safes, Gun Stores, Gunsmiths, Hobby Stores, Jewelers, Lighting Stores, Office Furniture, Pawn Brokers, Perfume Stores, Piano Tuning, Shoe Stores, Skate Shops, Sport Shop, Supplements, Toy Stores, Vape Stores, Watches & Repair, Attorneys, Bail Bonds, Blood Tests, Business Coach, Real Estate Agents, Real Estate Brokers, Salvage Yards."
    ],
    "Open Pool (after NOs)": [
      "IT managed services and infrastructure: MSPs, cybersecurity/compliance, ISPs, POS/IT integration, network cabling/telecom (prefer recurring contracts/SLAs; manager-led; avoid pure software and heavy one-time project mixes).",
      "Home services and specialty contractors: HVAC service and light install, electrical service, garage doors and gates, fencing, pool service routes, roofing service/maintenance (commercial focus), parking lot striping and sealcoating. Plumbing only if a licensed leader is in place.",
      "Commercial facility services: janitorial, floor care, day porter, window cleaning, pressure washing, commercial landscaping and irrigation (recurring contracts).",
      "Niche printing and signage: wide-format printing, environmental graphics, screen printing, custom signs, sign fabrication and install, print finishing services.",
      "Light manufacturing and fabrication: custom metal or wood components, simple assemblies, packaging or kitting, contract light manufacturing with predictable capex.",
      "B2B distribution (niche, non-commodity): MRO supplies, industrial parts, safety or specialty fasteners, electrical or HVAC parts distribution with stable margins.",
      "Insurance agencies: P&C retail agencies or benefits-focused shops with recurring commissions; clean retention and cross-sell potential.",
      "Home health care: non-medical personal care or skilled home health with strong billing, compliance, and caregiver pipeline.",
      "Transportation and storage (light): last-mile routes, niche logistics, small 3PL/warehouse services with steady contracts and simple operations.",
      "Trucking and diesel services (local): multi-line operators (repair shop, retail, trucking) where the owner can stay on; bring an industry expert if advancing.",
      "Route-based services: document shredding, medical waste pick-up (light compliance only), linen and mat service if capex is manageable.",
      "Equipment services: maintenance, repair, or rental of light equipment with predictable utilization and service contracts.",
      "Pet services (select): boarding, daycare, or grooming with manager-led operations and steady membership or recurring bookings.",
      "Fitness (select): membership-driven studios with manager-led teams and stable recurring revenue.",
      "Commercial specialty trades with licensing covered by staff leadership: fire sprinkler inspection excluded if heavy compliance; consider only if compliance burden is light and leader is in seat.",
      "Business services with repeat B2B demand: safety training services, compliance light testing, calibration or certification services where regulation is minimal and repeat cycles exist.",
      "Seasonal services with multi-year contracts: snow removal equivalents not common in DFW; focus on hot-weather analogs like HVAC maintenance plans and landscaping renewals.",
      "Home-based, capital-light service aggregator platforms (e.g., dumpster provider network) if tech-light, defensible, and not exposed to AI/online risk.",
      "Select strategic, retainer‑based marketing agencies in durable niches (AI‑resistant) — only if a strong GM/#2 runs day to day."
    ]
  },
  "15) Client-Stated Excitement (ranked list)": {
    "Table": [
      {
        "Rank": "1",
        "Industry / Model": "Remote, tech‑light, manager‑led businesses",
        "Why client is excited (quote/summary)": "“We love remote, 100%… If it’s remote and not tech, we’re all for it.” “If it’s remote and requires less of your time… we’d go higher on multiple.”",
        "Notes / caveats": "Avoid tech/SaaS due to AI risk. Higher multiple only if time load is truly low and operations are stable."
      },
      {
        "Rank": "2",
        "Industry / Model": "Asset‑light, remote‑friendly B2B distributor (little or no inventory)",
        "Why client is excited (quote/summary)": "“I loved it. I loved the idea of owner working remote from Florida.” “I loved the EBITDA of a million.” “It was a distributor… they don’t have any inventory.” “If we can find anything remotely close to that, that would be amazing.”",
        "Notes / caveats": "Not dropshipping; they avoid dropshipping and e‑commerce. Target tech‑light distributors with low AI exposure and little or no inventory; remote okay if controls are strong. They liked a ~3.7x multiple and ~$1M EBITDA example."
      },
      {
        "Rank": "3",
        "Industry / Model": "Home services trades with licensed leader (HVAC, electrical)",
        "Why client is excited (quote/summary)": "“We can leverage AI to improve these, but you still need a physical [person] to do these.” “For the right (profitable) business we would consider getting the required license.”",
        "Notes / caveats": "Prefer an in‑place license holder or #2. Plumbing is uncertain due to long licensing timelines. Nov 4 (electrical deal): Juan said the lack of new‑construction work is “super, super interesting… a huge opportunity,” so they are excited to add that line if a strong non‑compete protects scope and a master electrician is secured (retain or hire)."
      },
      {
        "Rank": "4",
        "Industry / Model": "Home health care (insurance‑billed, non‑medical or skilled)",
        "Why client is excited (quote/summary)": "“This is the only one we would feel comfortable doing medical‑related business in.” “You are billing insurance and it can get very recurring.”",
        "Notes / caveats": "They have personal family experience and like the recurring, insurance‑paid model. Want solid billing and clean compliance."
      },
      {
        "Rank": "5",
        "Industry / Model": "Insurance agencies (P&C or benefits)",
        "Why client is excited (quote/summary)": "“I work with an insurance agent… I see the potential there and I see that that’s something that we could get behind.” “Yes, I would be interested [in a license] if needed.”",
        "Notes / caveats": "Drawn to recurring commissions and cross‑sell. Open to licensing if it makes sense."
      },
      {
        "Rank": "6",
        "Industry / Model": "Niche printing and signage (wide‑format, environmental graphics, screen printing)",
        "Why client is excited (quote/summary)": "“What AI can’t do is print.” “We were just in Walmart last week and I told Mollie, I wonder who is printing these?”",
        "Notes / caveats": "Kept banner printing and screen printing open. Like physical output, low AI threat, and room to modernize with tech."
      },
      {
        "Rank": "7",
        "Industry / Model": "Light manufacturing and fabrication (non‑commodity)",
        "Why client is excited (quote/summary)": "Client kept “everything else open” in manufacturing and reacted, “Oh, I love it,” when reviewing the category.",
        "Notes / caveats": "They excluded clothing/footwear and chips due to “race to the bottom” and complexity. Prefer simple, steady ops with clear margins."
      },
      {
        "Rank": "8",
        "Industry / Model": "B2B services with recurring revenue and low competition",
        "Why client is excited (quote/summary)": "“We want to be able to grow the business and not be pinching for margins or have too much pressure from competitors.”",
        "Notes / caveats": "Favor steady contracts, repeat customers, and calm markets. Avoid heavy cold‑calling and high‑pressure rival battles."
      },
      {
        "Rank": "9",
        "Industry / Model": "Off‑market and broker‑network first‑look deals (sourcing model)",
        "Why client is excited (quote/summary)": "“I’m extremely interested in those deals that are made available to brokers first… and the off‑market ones… those are probably the ones that I would say I am the most interested in.”",
        "Notes / caveats": "Want deals that don’t hit public sites. Expect better terms and faster paths if sourced through networks."
      },
      {
        "Rank": "10",
        "Industry / Model": "Businesses with room to digitize and modernize (CRM, pricing, website, basic AI for ops)",
        "Why client is excited (quote/summary)": "“Digitizing would be something that we’d be looking to explore.” “We can figure out any software.” “I implemented a software that does revenue management for pricing.” “Probably every meeting I’ve had today, I’ve used ChatGPT… I was brainstorming with it… it’s truly like doing my job. I’m guiding it, but it’s doing my job.”",
        "Notes / caveats": "They want quick, low‑risk wins post‑close: CRM, pricing tools, site refresh, brand and demand engine."
      },
      {
        "Rank": "11",
        "Industry / Model": "Businesses with a strong #2 or operator in place",
        "Why client is excited (quote/summary)": "“A good lieutenant, a number two.” “It would be ideal to have an operator in place.”",
        "Notes / caveats": "Long‑term goal is manager‑led. They will work hard early, then step down to healthier hours."
      },
      {
        "Rank": "12",
        "Industry / Model": "Retiring owner, non‑compete, and clear growth levers",
        "Why client is excited (quote/summary)": "“Someone who is retiring… and where there’s room for growth, either through digitizing…”",
        "Notes / caveats": "Prefer sellers who won’t compete. Open to short or longer transition as needed. Growth focus after learn‑and‑maintain phase."
      },
      {
        "Rank": "13",
        "Industry / Model": "Flexible, buyer‑friendly structures (seller carry, standby notes)",
        "Why client is excited (quote/summary)": "“We got it 100% seller financing… we wanted to move quick.” “We would love to get seller financing… 10%, 20%.” “We would be open to a 90‑10 split… 90% of something is better than nothing… we’re open.”",
        "Notes / caveats": "Comfortable with SBA plus seller note on standby to boost equity. Open to small seller rollover equity (~10%) if allowed under SBA; needs clarity on 51% control and whether the seller must PG. Avoid ROBS unless a true unicorn."
      },
      {
        "Rank": "14",
        "Industry / Model": "Businesses with backlog or booked work runway",
        "Why client is excited (quote/summary)": "“They already have like $5 million in queue… I like that, having a runway… If you buy in, you’re already off to a good start.”",
        "Notes / caveats": "Want clear, legit backlog that rolls into next year; will verify in updated TTM and broker call."
      },
      {
        "Rank": "15",
        "Industry / Model": "Larger businesses where the same effort yields higher returns",
        "Why client is excited (quote/summary)": "“The amount of effort we would put into here could also be put into a bigger company where we can make more… there’s more meat on the bone.”",
        "Notes / caveats": "Will pass on small, one‑man shops that miss the income bar even if the people fit is strong. Bigger is fine when DSCR and time load work."
      },
      {
        "Rank": "16",
        "Industry / Model": "Home‑based, capital‑light service aggregator platforms (vendor‑to‑contractor networks, e.g., dumpster provider network)",
        "Why client is excited (quote/summary)": "“Home‑based. We would love that.” “It’s not capital intensive at all… it’s a platform connecting dumpster [providers] to builders.”",
        "Notes / caveats": "Prefer ≤4x multiple; will not chase ~5x asks. Must be tech‑light, defensible, and low AI/online risk; remote/home‑based day‑to‑day is a plus."
      },
      {
        "Rank": "17",
        "Industry / Model": "Select strategic, retainer‑based marketing agencies (AI‑resistant) with a strong GM/#2",
        "Why client is excited (quote/summary)": "“It could be cool to see what that could look like.” “If it’s a marketing agency, I feel like I would just be buying my job… would love… a strong number two… so we can steer and guide it, not work it full‑time.” “Instead of ‘AI replaces it,’ think about how we can leverage [AI] to grow the business.”",
        "Notes / caveats": "Newly open only if work is AI‑resistant (strategy on retainers in durable niches) and a manager runs day‑to‑day. Avoid production‑only work that AI can replace. Keep SDE and DFW‑first guardrails."
      },
      {
        "Rank": "18",
        "Industry / Model": "IT managed services and infrastructure (MSP, cybersecurity/compliance, ISP, POS/IT integration, network cabling/telecom)",
        "Why client is excited (quote/summary)": "“We’d like to include the following categories in our search going forward” to boost deal flow. Drawn to recurring contracts and stable, manager‑led ops.",
        "Notes / caveats": "Pilot addition. Prefer recurring contracts/SLAs and a strong GM/ops lead. Avoid pure software and heavy one‑time projects. Keep SDE and DFW‑first guardrails; apply AI‑risk and bankability screens."
      }
    ]
  },
  "16) Recommended Business Types": {
    "16.1 Best-Suited Categories": [
      "HVAC service and light installs (DFW focus): recurring maintenance plans; licensing can be covered by an in-place leader; easy wins with pricing, scheduling, and CRM.",
      "Electrical service and small projects: steady demand; strong upsell path with preventive maintenance; process and branding upgrades fit your strengths. Plan for license coverage: retain an internal master electrician candidate or hire an outside master before close; seller can stay short-term. Add inbound marketing (today is mostly referrals/bids). Require a solid non-compete given the seller’s new‑construction plans.",
      "Niche printing and signage (wide-format, environmental graphics, screen printing, custom sign fab and install): clear fit for Mollie’s brand, GTM, and ops; repeat B2B orders; local relationships; add CRM, SEO-lite, and sales process.",
      "Commercial facility services (janitorial, floor care, day porter, window cleaning, pressure washing): contract-based revenue; ops cadence matches your experience; upsell paths across services.",
      "B2B distribution (niche, non-commodity such as MRO, specialty fasteners, safety, HVAC or electrical parts): repeat customers; margin protection in niches; asset-light with low or no inventory where possible; remote-manageable; improve pricing, inventory turns, and account growth.",
      "IT managed services and infrastructure (MSPs, cybersecurity/compliance, ISPs, POS/IT integration, network cabling/telecom): recurring contracts and SLAs; manager-led day to day; maps to your ops, pricing, and account management strengths; avoid pure software and heavy one-time project mixes.",
      "Insurance agencies (P&C retail or employee benefits): recurring commissions; cross-sell playbook; Juan’s finance and negotiation skills shine; potential roll-up.",
      "Home health care (non-medical personal care or skilled home health): mission fit; insurance billing; retention and caregiver pipeline improvements; controlled growth with compliance discipline.",
      "Light manufacturing and fabrication (simple assemblies, custom metal/wood, kitting, contract light manufacturing): stable B2B demand; scheduling and cost control fit your strengths; measured capex.",
      "Glazing and window coverings (glass/glazier and blinds) fabrication and install: backlog-driven B2B bids; strong fit for process and scheduling; verify TTM vs prior year, backlog quality, and lease vs buy real estate; assess daily presence need and strength of a #2; site up to ~2.5 hours OK if team is self-sufficient.",
      "Route-based services (document shredding, medical waste pick-up with light compliance, linen and mat service if capex manageable): predictable routes; recurring revenue; simple KPIs; upsell new accounts.",
      "Equipment services (maintenance, repair, or rental of light equipment): service contracts; utilization levers; easy to add PM schedules and digital dispatching.",
      "Transportation and storage (light) such as last‑mile routes, niche logistics, small 3PL/warehouse: contract stability; ops and process upgrades; scalable with systems.",
      "Select pet services (boarding, daycare, grooming): manager-led model; recurring membership revenue; brand and experience lift.",
      "Select fitness (membership-driven studios with a manager): recurring dues; brand and lifecycle marketing fit; must be manager-led and stable."
    ],
    "16.2 Strategic Opportunities": [
      "New-construction electrical build-out (as an add-on to an electrical service company): large bid market; pursue only after securing a strong non-compete with the seller and placing a master electrician; start with selective GC partners and clear margin targets.",
      "Pest control (licensing manageable): recurring routes; strong retention; simple KPI model.",
      "Pool service routes (residential or commercial): recurring service; route density; easy to add chem bundles and repairs.",
      "Parking lot striping and sealcoating: B2B repeat need; seasonal schedules; quoting and routing efficiency win.",
      "Garage doors and gates (residential or light commercial): service plus installs; parts margin; dispatch and marketing lift.",
      "Fencing service and repair (commercial focus): steady bids; add maintenance plans and access control upsells.",
      "Commercial landscaping and irrigation (contracts-first): recurring revenue; add enhancements and irrigation service plans.",
      "Window cleaning and high-dusting (commercial): recurring schedules; fast wins with route density and add-on services.",
      "Document shredding and records destruction: compliance-light; long-term contracts; route and plant efficiency.",
      "Medical waste pick-up (light compliance only): recurring customers; predictable routes; regulated moat without heavy burden.",
      "Safety training or compliance-light testing (calibration, certification services): repeat cycles; B2B relationships; strong gross margin.",
      "Sign maintenance and lighting retrofit: recurring service; add LED retrofit programs; cross-sell with graphics.",
      "Specialty fastener or safety supply distribution: niche SKUs; loyal accounts; upsell kits and replenishment programs.",
      "Small 3PL with value-add (kitting, light assembly): sticky B2B clients; process and SLA reliability; expands with sales.",
      "Trucking and diesel services (edge case): only consider if the owner stays on as a #2 to run day to day, no new build-out loans (no gas station/strip mall add-ons), and pay is handled through price/structure (for example, salary plus a performance note). Bring an industry expert if advancing.",
      "Portable storage or light equipment rental: recurring rental cycles; utilization levers; service add-ons.",
      "Roofing and restoration (commercial service/maintenance focus): inspection and maintenance agreements; avoid storm-chasing model.",
      "Parking lot sweeping and porter services: predictable night routes; contracts; upsell to striping and pressure washing.",
      "Home-based, capital-light service aggregator (e.g., dumpster provider network): asset-light and remote; connects suppliers to builders; simple ops fit. Only if tech-light and defensible (low AI risk). Hold price discipline (aim ≤4x multiple). Watch broker terms and NDAs.",
      "Select strategic, retainer-based marketing agencies in durable niches (AI-resistant): only if a strong GM or #2 runs day to day; prefer retainer relationships and high-level strategy; avoid project-only, low-level production work."
    ],
    "16.3 Avoid Categories": [
      "Car Dealerships: heavy sales pressure and floorplan risk; not aligned with lifestyle.",
      "RV Dealers: high inventory and cyclicality; sales pressure.",
      "Coolsculpting: trend-driven; regulatory and clinical risk.",
      "Cosmetic & Plastic Surgery: medical licensing and liability.",
      "Hair Salons: low ticket and high labor scheduling; thin margins.",
      "Nail Salons: low ticket and labor-heavy; weekend demand.",
      "Weight Loss: gimmick risk; churn and compliance concerns.",
      "Advertising & Design: high AI disruption and price pressure.",
      "Advertising Agency: AI and copycat exposure; client churn risk.",
      "Digital Marketing: AI displacement; race-to-the-bottom fees.",
      "Internet Publishers: ad-market volatility; SEO and AI risk.",
      "Newspapers: structural decline; ad dependence.",
      "Periodicals & Magazine Publishers: declining print; ad risk.",
      "Radio Stations: declining audience; ad headwinds.",
      "SEO Companies: AI-driven commoditization.",
      "Television Stations: high cost; ad market risk.",
      "Web Design & Development: AI tools commoditize work.",
      "Adoption Agency: high regulation and legal complexity.",
      "Dance Studios: low ticket and high churn; schedule-heavy.",
      "Tutoring: AI tutor replacement; model risk.",
      "Tutoring Centers: AI displacement; lease and staffing load.",
      "Seminars: one-time revenue; marketing-heavy churn.",
      "Specialized/Career Education: regulatory risk; AI shift.",
      "Teachers: not a business acquisition target for them.",
      "Virtual/Online Learning: AI competition; platform risk.",
      "Vocational Trades Education: compliance; enrollment risk.",
      "Amusement Parks: liability, capex, and seasonality.",
      "Antique Dealers: discretionary, slow turns; niche demand.",
      "Escape Rooms: fad risk; frequent refresh capex.",
      "Magicians: owner-operator dependent; non-transferable.",
      "Nightclubs & Theaters: late hours; regulatory risk; labor heavy.",
      "Psychics: not values-aligned; demand volatility.",
      "Tattoo Studios: owner-artist keyed; lifestyle mismatch.",
      "Videography: AI tools erode pricing; gig-based demand.",
      "Accounting & Tax Services: AI automation and pricing pressure.",
      "Bookkeeping: AI and software automation; fee compression.",
      "Brokerage & Security Dealers: heavy compliance and licensing.",
      "Check Cashing: regulatory and reputational risk.",
      "Collection Agencies: compliance and reputational risk.",
      "Crypto Related: high volatility; regulatory uncertainty.",
      "Factoring: credit risk; regulatory and complexity not desired.",
      "Addiction Treatment Center: clinical and regulatory burden.",
      "Cardiologist: physician model; licensing liability.",
      "Chiropractors: clinical licensing; owner-key risk.",
      "Counselors: licensing and owner-operator dependence.",
      "Dental Services: doctor dependency; clinical liability.",
      "Dermatologists: physician-dependent; high regulatory burden.",
      "Dietitians: low ticket; licensing and churn.",
      "Doctors: clinical dependency; liability and compliance.",
      "Hearing Aid Store: medical device rules; sales pressure.",
      "Hospitals: extreme regulation and capital intensity.",
      "Hypnotherapists: niche demand; owner-driven.",
      "Laser Eye: clinical liability; capex; licensing.",
      "Lasik: physician-dependent; high capex and marketing pressure.",
      "Massage: licensing and liability; weekend-heavy hours.",
      "Nutritionists: low ticket and churn; owner-led.",
      "Optical Services: licensing; retail inventory risk.",
      "Pediatricians: physician-dependent; liability.",
      "Physical Therapists: compliance and payer complexity.",
      "Psychiatrists: medical compliance; owner-keyed.",
      "Psychologists: licensing; owner-operator model.",
      "Psychotherapists: owner-operator; compliance.",
      "Rehab: clinical risk; heavy regulation.",
      "Speech Therapists: licensing; payer mix complexity.",
      "Telehealth: tech and regulatory risk; platform competition.",
      "Urologists: physician-dependent; liability.",
      "Vein Clinic: medical risk; marketing-heavy; capex.",
      "Acupuncture: licensing; owner-operator model.",
      "Clothing & Footwear Manufacturing: low margins; global competition.",
      "Computer & Chip Manufacturing: extreme capex; global competition.",
      "Content sites (affiliate/advertising): SEO and AI disruption.",
      "Digital products: copycat and AI risk; platform dependence.",
      "Dropshipping: race to the bottom; platform risk.",
      "eCommerce/Amazon FBA: copycat, margin squeeze, and platform risk.",
      "KDP businesses: platform and AI content saturation.",
      "Mobile Apps: high tech risk; platform dependence.",
      "SAAS: AI disruption; heavy engineering and churn risk.",
      "Web Design & Development (service): AI commoditization; low defensibility.",
      "Computer Repair: declining demand; price pressure.",
      "Computer Store: inventory risk; thin margins.",
      "Network Consultants: project-based, competitive; tech change risk.",
      "Point of Sale Systems: vendor-controlled; tech disruption.",
      "Veterinarians: doctor-dependent; clinical liability.",
      "Bakeries: low margins; early hours; perishables.",
      "Bars: late nights; compliance and labor risk.",
      "Breweries: capex-heavy; distribution risk.",
      "Cafes: thin margins; labor-heavy; long hours.",
      "Catering Services: event cyclicality; labor intensive.",
      "Coffeeshops, Cafes & Dessert Shops: low margin; long hours.",
      "Convenience Stores: low margins; shrink and inventory risk.",
      "Food & Beverage: thin margins; labor and spoilage.",
      "Food & Beverage Distribution & Routes: margin pressure; working capital heavy.",
      "Food Production & Packaging: capex and compliance; tight margins.",
      "Food Trucks: seasonal; site and labor heavy.",
      "Grocery & Supermarkets: low margin; inventory and shrink.",
      "Juice Bar: fad risk; low margins; labor-heavy.",
      "Liquor & Wine: licensing; inventory and theft risk.",
      "Liquor Licenses: regulatory complexity; limited value.",
      "Mexican Restaurants: category-wide issues (margins, hours).",
      "Pizzerias: low margin; late hours; turnover.",
      "Restaurants: low margins; weekend and night hours.",
      "Sandwich Bar: thin margins; high labor.",
      "Sushi Restaurants: perishables; food safety risk.",
      "Takeaway Restaurant: low margin; competition heavy.",
      "Vegan Restaurants: niche demand; margin issues.",
      "Vending Machines: small ticket; scale needed; logistics.",
      "Appliance Repair: scheduling volatility; weekend demand; low average ticket.",
      "Bedding Store: inventory and markdown risk; foot traffic dependence.",
      "Bicycle Store: inventory heavy; seasonal.",
      "Bookstores: low margin; e‑commerce pressure.",
      "Boutique: fashion risk; inventory markdowns.",
      "Bridal Shop: seasonality; inventory and fittings complexity.",
      "Camping Stores: seasonal; inventory risk.",
      "Car Decals: low barrier; price pressure.",
      "Card & Stationery Stores: low margin; declining foot traffic.",
      "Cash for Gold: reputational and regulatory risk.",
      "Childrens Clothing Stores: inventory and markdown risk.",
      "Clothes Retail: inventory risk; race to bottom.",
      "Craft Supplies: big-box competition; inventory burden.",
      "Electronics Store: thin margins; obsolescence.",
      "Embroidery Services: commoditized; price pressure.",
      "Fabric Shops: slow turns; niche demand.",
      "Fishing Supplies: seasonal; inventory risk.",
      "Flooring: inventory, install complications; thin margins in retail model.",
      "Furniture Stores: high ticket plus inventory and returns risk.",
      "Garden Centeres and nurseries: seasonal; shrinkage; weather risk.",
      "Gift Shops: discretionary; low margins.",
      "Gun Safes: niche; regulatory and delivery complexity.",
      "Gun Stores: regulatory risk; inventory and liability.",
      "Gunsmiths: owner-skill dependent; low throughput.",
      "Hobby Stores: discretionary; online competition.",
      "Jewelers: theft and inventory risk; slow turns.",
      "Lighting Stores: inventory-heavy; showroom costs.",
      "Office Furniture: B2B but inventory and price pressure.",
      "Pawn Brokers: regulatory and reputational risk.",
      "Perfume Stores: counterfeits risk; inventory heavy.",
      "Piano Tuning: owner-operator; low scalability.",
      "Shoe Stores: inventory and size complexity; low margins.",
      "Skate Shops: niche; inventory risk.",
      "Sport Shop: seasonal; inventory pressure.",
      "Supplements: compliance and competition; quality risk.",
      "Toy Stores: seasonal; inventory and trend risk.",
      "Vape Stores: regulatory risk; product volatility.",
      "Watches & Repair: theft risk; niche; inventory.",
      "Attorneys: licensing and model mismatch.",
      "Bail Bonds: regulatory and reputational risk.",
      "Blood Tests: medical compliance; liability.",
      "Business Coach: AI coaching pressure; person-keyed.",
      "Real Estate Agents: licensing; commission cyclicality.",
      "Real Estate Brokers: commission volatility; recruiting treadmill.",
      "Salvage Yards: environmental compliance; heavy operations."
    ]
  },
  "17) Analyst/AI Fit Recommendations — Ranked Top 20": {
    "Table": [
      {
        "Rank": "1",
        "Industry / Model": "Asset-light, remote-friendly B2B distributor (low or no inventory; not e-commerce/dropship)",
        "Why it fits (1–2 lines)": "Strong excitement for a tech-light distributor the owner can run remotely; example they loved was ~$1M EBITDA at ~3.7x with little to no inventory. Clear fit for pricing, CRM, and account growth.",
        "Key match factors": [
          "Remote owner model viable",
          "Low inventory working capital",
          "Pricing and segmentation upside",
          "DFW or remote with local fulfillment"
        ],
        "Risk flags": "Supplier and customer concentration; key vendor dependence. Risk adj -0.2",
        "Score": "Final 4.64. Fit 4.8, Exc 4.9, Risk -0.2"
      },
      {
        "Rank": "2",
        "Industry / Model": "HVAC service and maintenance with licensed leader retained",
        "Why it fits (1–2 lines)": "High need in DFW, strong maintenance plan revenue, clear levers to digitize pricing, CRM, and inbound. They can manage ops while a licensed manager covers permits.",
        "Key match factors": [
          "DFW density and routes",
          "Recurring maintenance plans",
          "Clear digitize and marketing upside",
          "Fits $750k+ SDE band"
        ],
        "Risk flags": "Seasonality and tech labor availability. Risk adj -0.3",
        "Score": "Final 4.58. Fit 5.0, Exc 4.7, Risk -0.3"
      },
      {
        "Rank": "3",
        "Industry / Model": "Electrical service and maintenance with master electrician on staff",
        "Why it fits (1–2 lines)": "Active DFW focus aligns with their skills. Less seasonality than HVAC, strong add-ons and service plans, plus clear upside adding new-construction work if a tight non-compete protects scope.",
        "Key match factors": [
          "License coverage via internal candidates or hiring an outside master electrician",
          "Service plans and inbound marketing lift",
          "Negotiation strength for B2B accounts",
          "Potential to add new-construction if protected by non-compete"
        ],
        "Risk flags": "License holder dependency and hiring risk; referral-partner concentration vs a single client requires diversification; must secure a strong non-compete if seller pursues new-construction. Risk adj -0.3",
        "Score": "Final 4.42. Fit 4.8, Exc 4.6, Risk -0.3"
      },
      {
        "Rank": "4",
        "Industry / Model": "Niche printing and signage wide-format, environmental graphics, fabrication",
        "Why it fits (1–2 lines)": "Physical output not threatened by AI. Obvious room to modernize quoting, CRM, and web presence, and upsell install services.",
        "Key match factors": [
          "Low AI risk",
          "B2B repeat orders",
          "DFW demand in retail and facilities",
          "Brand and sales engine upgrade"
        ],
        "Risk flags": "Project cyclicality and some capex. Risk adj -0.2",
        "Score": "Final 4.36. Fit 4.6, Exc 4.5, Risk -0.2"
      },
      {
        "Rank": "5",
        "Industry / Model": "Insurance agencies P and C retail with solid book and retention",
        "Why it fits (1–2 lines)": "Recurring commissions, cross-sell, and strong lifetime value. Open to licensing and like the model.",
        "Key match factors": [
          "Recurring revenue",
          "Cross-sell playbook",
          "Process and data strengths",
          "Roll-up potential"
        ],
        "Risk flags": "Licensing and carrier compliance. Risk adj -0.2",
        "Score": "Final 4.32. Fit 4.4, Exc 4.7, Risk -0.2"
      },
      {
        "Rank": "6",
        "Industry / Model": "Calibration, testing, and certification services compliance light",
        "Why it fits (1–2 lines)": "Repeat cycles and B2B stickiness with low AI risk. Great fit for process and relationship skills.",
        "Key match factors": [
          "Repeat contracts",
          "Light regulation",
          "Process improvement wins",
          "Easy to digitize pipeline"
        ],
        "Risk flags": "Some key techs and customers concentrated. Risk adj -0.1",
        "Score": "Final 4.14. Fit 4.4, Exc 4.0, Risk -0.1"
      },
      {
        "Rank": "7",
        "Industry / Model": "Garage doors and gates service and light install",
        "Why it fits (1–2 lines)": "Route density, service plans, and upgrade sales. Simple ops with clear local demand.",
        "Key match factors": [
          "DFW route density",
          "Strong service plan fit",
          "Phone and web lead upgrades",
          "Quick dispatch process wins"
        ],
        "Risk flags": "Cyclical install mix and labor. Risk adj -0.3",
        "Score": "Final 4.08. Fit 4.5, Exc 4.2, Risk -0.3"
      },
      {
        "Rank": "8",
        "Industry / Model": "Pool service routes with add-on repairs",
        "Why it fits (1–2 lines)": "Recurring routes and predictable cash flow. Easy to brand, price, and optimize scheduling.",
        "Key match factors": [
          "Recurring route revenue",
          "Simple ops and routing",
          "Pricing and CRM lift",
          "Strong household market"
        ],
        "Risk flags": "Summer-heavy demand and turnover. Risk adj -0.2",
        "Score": "Final 4.06. Fit 4.3, Exc 4.2, Risk -0.2"
      },
      {
        "Rank": "9",
        "Industry / Model": "IT managed services and infrastructure MSP cybersecurity and compliance ISP POS and IT integration network cabling and telecom",
        "Why it fits (1–2 lines)": "Recurring contracts with SLAs and remote-friendly oversight fit their strengths in ops, pricing, and account growth. Newly in scope to boost deal flow while staying tech-light on delivery.",
        "Key match factors": [
          "Recurring revenue and SLAs",
          "Manager-led tech teams",
          "Cross-sell security and compliance",
          "Remote dashboards and ticketing KPIs",
          "DFW-first with field techs"
        ],
        "Risk flags": "On-call and after-hours demands, project-heavy mix, key client concentration. Risk adj -0.3",
        "Score": "Final 4.00. Fit 4.5, Exc 4.0, Risk -0.3"
      },
      {
        "Rank": "10",
        "Industry / Model": "Document shredding routes",
        "Why it fits (1–2 lines)": "Contracted B2B service with route density and recurring schedules. Low AI risk and simple compliance.",
        "Key match factors": [
          "Contracted routes",
          "Sticky B2B clients",
          "Route optimization",
          "Cross-sell bins and purge events"
        ],
        "Risk flags": "Truck capex and some safety compliance. Risk adj -0.2",
        "Score": "Final 3.98. Fit 4.3, Exc 4.0, Risk -0.2"
      },
      {
        "Rank": "11",
        "Industry / Model": "B2B distribution niche MRO, fasteners, safety, non-commodity",
        "Why it fits (1–2 lines)": "Steady repeat orders and relationship value. Their pricing, segmentation, and ops can boost margins.",
        "Key match factors": [
          "Repeat B2B demand",
          "Data driven pricing",
          "Add light ecommerce without platform risk",
          "Operational process wins"
        ],
        "Risk flags": "Inventory needs and concentration risk. Risk adj -0.3",
        "Score": "Final 3.94. Fit 4.4, Exc 4.0, Risk -0.3"
      },
      {
        "Rank": "12",
        "Industry / Model": "Light manufacturing custom metal or wood components and simple assemblies",
        "Why it fits (1–2 lines)": "Client said they love this. Low AI pressure, clear process, quoting, and sales upgrades.",
        "Key match factors": [
          "Low tech risk",
          "Steady B2B orders",
          "SOP and scheduling uplift",
          "Brand and quoting refresh"
        ],
        "Risk flags": "Capex and skilled labor. Risk adj -0.3",
        "Score": "Final 3.94. Fit 4.2, Exc 4.3, Risk -0.3"
      },
      {
        "Rank": "13",
        "Industry / Model": "Home health care non-medical personal care or skilled with clean billing",
        "Why it fits (1–2 lines)": "Only health vertical they want. Insurance billed, recurring visits, and strong mission fit.",
        "Key match factors": [
          "Recurring schedules",
          "Insurance billing strength",
          "Deep caregiver process focus",
          "Personal motivation"
        ],
        "Risk flags": "Compliance, caregiver churn, audits. Risk adj -0.5",
        "Score": "Final 3.90. Fit 4.2, Exc 4.7, Risk -0.5"
      },
      {
        "Rank": "14",
        "Industry / Model": "Parking lot striping and sealcoating",
        "Why it fits (1–2 lines)": "B2B maintenance with repeat cycles. Easy quoting, routing, and upsell to signage and repairs.",
        "Key match factors": [
          "Contract renewals",
          "Night crew friendly ops",
          "Estimating and CRM upgrades",
          "Cross-sell lots and markings"
        ],
        "Risk flags": "Weather windows and seasonality. Risk adj -0.3",
        "Score": "Final 3.84. Fit 4.3, Exc 3.9, Risk -0.3"
      },
      {
        "Rank": "15",
        "Industry / Model": "Commercial janitorial and day porter with contracts",
        "Why it fits (1–2 lines)": "Recurring contracts and account management play. Process and people leadership fit well.",
        "Key match factors": [
          "Contract revenue",
          "Route and crew scheduling",
          "KPI and QA programs",
          "Cross-sell floor care and windows"
        ],
        "Risk flags": "Labor intensity and churn. Risk adj -0.4",
        "Score": "Final 3.64. Fit 4.2, Exc 3.8, Risk -0.4"
      },
      {
        "Rank": "16",
        "Industry / Model": "Equipment maintenance or light rental service focused",
        "Why it fits (1–2 lines)": "Service contracts on small equipment and tools. Operations and pricing processes can drive lift.",
        "Key match factors": [
          "Service contracts",
          "Utilization tracking",
          "Parts pricing and inventory",
          "Technician routing"
        ],
        "Risk flags": "Capex and maintenance risk. Risk adj -0.3",
        "Score": "Final 3.62. Fit 4.0, Exc 3.8, Risk -0.3"
      },
      {
        "Rank": "17",
        "Industry / Model": "Commercial glazing and blinds fabrication and install (DFW example)",
        "Why it fits (1–2 lines)": "Clear marketing levers and fit, but timing is lower now because the broker suspended the sale until 2026. Distance works only if the team is self-sufficient.",
        "Key match factors": [
          "B2B bids and backlog",
          "Brand and inbound lift",
          "Scheduling and SOP upgrades",
          "Seller or #2 can stay"
        ],
        "Risk flags": "Project cyclicality, backlog quality, slow broker updates and trust concerns, real estate decisions, sale suspended until 2026. Risk adj -0.5",
        "Score": "Final 3.58. Fit 4.2, Exc 3.9, Risk -0.5"
      },
      {
        "Rank": "18",
        "Industry / Model": "Window cleaning and pressure washing commercial",
        "Why it fits (1–2 lines)": "Simple recurring B2B work with route density, easy to brand and schedule.",
        "Key match factors": [
          "Contract renewals",
          "Route planning",
          "Sales and inbound uplift",
          "Add-on surfaces"
        ],
        "Risk flags": "Weather and safety risk. Risk adj -0.3",
        "Score": "Final 3.58. Fit 4.0, Exc 3.7, Risk -0.3"
      },
      {
        "Rank": "19",
        "Industry / Model": "Trucking and logistics (local) with owner staying on",
        "Why it fits (1–2 lines)": "Revisit possible on a DFW deal with ~$1.2M SDE where the owner wants to stay post-close. Could de-risk handoff if the seller becomes the #2 while they install pricing, routing, and KPI rhythms.",
        "Key match factors": [
          "Seller willing to stay reduces transition risk",
          "Strong SDE and margin base",
          "Process, dispatch, and dashboard upgrades fit skills",
          "Only consider focused ops with no new build-outs"
        ],
        "Risk flags": "Multi-line complexity and capex history; they will not take another build-out loan; owner-stay pay must come from price or structure; requested 2025 figures before engaging. Risk adj -0.4",
        "Score": "Final 3.42. Fit 3.9, Exc 3.7, Risk -0.4"
      },
      {
        "Rank": "20",
        "Industry / Model": "Select strategic, retainer-based marketing agencies in durable niches (AI-resistant) with a strong GM/#2",
        "Why it fits (1–2 lines)": "Newly open to this if the work is high-level strategy on retainers, not production only. Leverages their marketing strengths and can be remote if a strong manager runs day to day.",
        "Key match factors": [
          "Strategy and account leadership on retainers, not commodity production",
          "Durable niches with low churn",
          "Remote-friendly, manager-led day to day",
          "Use AI to improve delivery, reporting, and pricing"
        ],
        "Risk flags": "AI can replace production-only tasks; client concentration; risk of “buying a job” without a GM. Risk adj -0.3",
        "Score": "Final 3.20. Fit 3.8, Exc 3.3, Risk -0.3"
      }
    ]
  },
  "18) Low-Fit / Misfit (even if client says “open”)": {
    "Table": [
      {
        "Category": "Tech/online businesses (SaaS, apps, marketplaces, content sites)",
        "Why it’s a misfit (plain English)": "High AI risk; skills do not match engineering-heavy work; not the lifestyle they want",
        "Example red flags to watch": "Subscriptions or ad-only revenue, churn fights, product roadmaps, heavy dev needs, SEO or app store dependence"
      },
      {
        "Category": "Digital marketing, ad agencies, web design, SEO firms (production/project-heavy)",
        "Why it’s a misfit (plain English)": "AI replaces commodity work; churn and project spikes create pressure; would feel like “buying a job” without a strong GM. Only consider when work is strategic and retainer-based in durable niches with a manager running day to day.",
        "Example red flags to watch": "Project-only deliverables, no retainers, low-level content/website production, no GM/lead in seat, short contracts and high churn, heavy outbound to fill pipeline"
      },
      {
        "Category": "E‑commerce and Amazon FBA",
        "Why it’s a misfit (plain English)": "Copycat risk and race to the bottom; heavy working capital; platform control",
        "Example red flags to watch": "Amazon storefront reliance, thin margins, big inventory balances, slow turns, MAP wars, ads arms race"
      },
      {
        "Category": "Inventory‑heavy retail stores",
        "Why it’s a misfit (plain English)": "Low margin, seasonality, markdown risk; not scalable to income goal",
        "Example red flags to watch": "Large inventory on hand, high shrink/returns, foot traffic dependence, frequent promotions to move stock"
      },
      {
        "Category": "Restaurants, bars, cafes, food trucks, catering",
        "Why it’s a misfit (plain English)": "Nights and weekends, high turnover, thin margins; opposite of family goals",
        "Example red flags to watch": "Weekend and late-night peak hours, heavy labor scheduling, spoilage, health inspections, tip reliance"
      },
      {
        "Category": "Heavy clinical healthcare (dentists, PT, dermatology, vein/laser clinics, veterinarians)",
        "Why it’s a misfit (plain English)": "Requires doctors or long-path licenses; complex compliance and liability",
        "Example red flags to watch": "Owner-physician dependency, payer audits, malpractice insurance, credentialing, Stark/AKS concerns"
      },
      {
        "Category": "Tutoring, test prep, online education",
        "Why it’s a misfit (plain English)": "AI tutors and free tools erode value; high churn, ad spend needed",
        "Example red flags to watch": "One-time courses, SEO and PPC dependence, low retention, season-driven spikes, shifting curriculums"
      },
      {
        "Category": "High-pressure “storm chasing” or bid-war models (e.g., storm roofing, commodity contractors)",
        "Why it’s a misfit (plain English)": "Constant urgency and price fights drain energy; poor fit for calm, steady pace",
        "Example red flags to watch": "Revenue tied to storms or disasters, door knocking, emergency work spikes, insurance claim battles"
      },
      {
        "Category": "Project-only, lumpy-revenue manufacturers or installers with no sales team (often not SBA-bankable)",
        "Why it’s a misfit (plain English)": "Unpredictable cash flow and lender pushback; may require all-cash; no sales team means owner-dependent pipeline",
        "Example red flags to watch": "“All-cash only” because SBA declined, big one-off projects with gaps, owner just answers the phone, no sales team, national one-off bid work with lumpy revenue"
      },
      {
        "Category": "Boiler-room sales models (heavy cold-calling)",
        "Why it’s a misfit (plain English)": "Not their style; burns time and team; poor fit for family/lifestyle",
        "Example red flags to watch": "Daily dial quotas, new-logo targets >70% of revenue, commission-only culture, script-driven outreach"
      },
      {
        "Category": "Master-license trades that require owner license with long path (e.g., plumbing, fire sprinkler RME)",
        "Why it’s a misfit (plain English)": "Long licensing timeline traps owner; they prefer licensed #2 in place",
        "Example red flags to watch": "State rule that owner of record must hold license, no licensed foreman on staff, multi-year apprenticeship need"
      },
      {
        "Category": "Licensed trades without a secured license holder at or before close",
        "Why it’s a misfit (plain English)": "They will only proceed if a master license holder is in seat day one; unclear plans or “we hope someone passes the exam” is not enough",
        "Example red flags to watch": "No signed retention agreement with the license holder; candidates have not passed; no outside hire identified; seller won’t stay short-term to cover license"
      },
      {
        "Category": "Highly regulated financial services (broker/dealer, check cashing, collections, factoring, crypto)",
        "Why it’s a misfit (plain English)": "Heavy compliance, audits, reputation risk; not needed to hit goals",
        "Example red flags to watch": "FINRA/SEC oversight, BSA/AML audits, state MSB licensing, surety bonds, high complaint risk"
      },
      {
        "Category": "Night-and-weekend entertainment (nightclubs, event venues, theaters, amusement)",
        "Why it’s a misfit (plain English)": "Late hours and weekend peaks clash with family time; liability high",
        "Example red flags to watch": "Majority weekend revenue, alcohol permits, large crowds, security needs, high insurance costs"
      },
      {
        "Category": "Entertainment fads (escape rooms, VR arcades, novelty experiences)",
        "Why it’s a misfit (plain English)": "Trend risk and frequent refresh capex; revenue drops fast",
        "Example red flags to watch": "New buildouts often, refresh cycle every few months, heavy Groupon use, short booking windows"
      },
      {
        "Category": "Vending machines and small-ticket routes",
        "Why it’s a misfit (plain English)": "Needs huge scale to meet income target; logistics and theft risk",
        "Example red flags to watch": "Low revenue per machine, hundreds of sites needed, coin/cash handling, frequent restocking"
      },
      {
        "Category": "Heavy environmental or hazmat treatment operations (not simple pickup)",
        "Why it’s a misfit (plain English)": "Complex permits, high liability, large capex; outside comfort",
        "Example red flags to watch": "RCRA or EPA treatment permits, specialized equipment, spill risk, large compliance staff"
      },
      {
        "Category": "Single-person or artist-led businesses (owner is the product)",
        "Why it’s a misfit (plain English)": "Key-person risk; cannot replace the seller easily",
        "Example red flags to watch": "Revenue tied to owner’s name or skill, no SOPs, clients insist on seller, weak bench"
      },
      {
        "Category": "One-person owner-operator models with no team in place",
        "Why it’s a misfit (plain English)": "Requires building the whole team from scratch; same effort as a bigger deal but lower payoff; can miss their income bar",
        "Example red flags to watch": "Only the owner (and maybe spouse) does all work; no staff or ops bench; SDE relies on unpaid owner labor; would need to hire a GM or pay seller-as-#2 which cuts SDE below target"
      },
      {
        "Category": "Younger “builder” seller unwilling to sign a strong non‑compete or stay on in sales",
        "Why it’s a misfit (plain English)": "High risk of immediate competition post‑close; opposite of their preference to protect the transition",
        "Example red flags to watch": "Seller states plans to start a new shop soon; pursuing a new‑construction company in the same trade without tight non‑compete and carve‑outs; refuses a reasonable non‑compete or pushes broad carve‑outs; wants zero/very short transition; declines a commission‑based sales role"
      },
      {
        "Category": "Extreme seasonality businesses (holiday retail, ski/boat rentals)",
        "Why it’s a misfit (plain English)": "Cash swings and staffing pain; hard to keep steady DSCR",
        "Example red flags to watch": ">60% revenue in one season, big pre-season buys, short staffing windows, weather exposure"
      },
      {
        "Category": "Pure POS resellers or project-only IT services (no recurring contracts)",
        "Why it’s a misfit (plain English)": "Vendor control, rapid tech change, thin margins; no stable recurring revenue; would feel like “buying a job”",
        "Example red flags to watch": "Reliance on one vendor, hardware/software resale only, no MSP-style contracts/SLAs, heavy one-time installs/break-fix, churny project mix"
      },
      {
        "Category": "Real estate brokerage and agent shops",
        "Why it’s a misfit (plain English)": "Commission cycles and recruiting treadmill; not aligned with goals",
        "Example red flags to watch": "1099 agent churn, desk fees, split fights, market swings, high marketing spend for leads"
      },
      {
        "Category": "Low-margin commodity manufacturing (clothing, chip/computer parts)",
        "Why it’s a misfit (plain English)": "Global competition, capex, price wars; poor fit for risk profile",
        "Example red flags to watch": "Customer demands on price, long lead times, high WIP, import exposure, thin gross margin"
      },
      {
        "Category": "24/7 freight brokerages or dispatch (always-on ops)",
        "Why it’s a misfit (plain English)": "Nights, weekends, and constant fires; opposite of steady pace",
        "Example red flags to watch": "After-hours coverage required, tendering deadlines, load board dependence, razor-thin spreads"
      },
      {
        "Category": "Complex, multi-line “several businesses in one” (e.g., fleet + repair + new retail + fuel + real estate)",
        "Why it’s a misfit (plain English)": "Too many moving parts and split focus; feels like five jobs; not right for a first deal",
        "Example red flags to watch": "Separate units or P&Ls owning trucks plus a service shop; plans to build a retail strip center or gas station; real estate leasing included"
      },
      {
        "Category": "Deals that need big build-outs or extra loans at or right after close",
        "Why it’s a misfit (plain English)": "They do not want another loan for development; build-outs soak time and cash and raise risk",
        "Example red flags to watch": "Seller asks for a $2M+ injection for construction; strip‑mall or fuel station build tied to LOI; separate development loan needed to hit plan"
      },
      {
        "Category": "Businesses where the marketing path is unclear to them",
        "Why it’s a misfit (plain English)": "If they can’t see simple, practical marketing moves fast, confidence drops and it’s not a fit",
        "Example red flags to watch": "Can’t list 3–5 day‑1 marketing levers; heavy cold‑calling is the only path; no clear buyer persona; no simple inbound plan"
      },
      {
        "Category": "High customer or referral-channel concentration without a plan to diversify",
        "Why it’s a misfit (plain English)": "Too much revenue tied to one partner or a few referral sources risks sudden drops",
        "Example red flags to watch": "One partner >30% of revenue; top 3 >45–50% combined; informal referral ties with no contracts; no marketing engine to broaden the base"
      },
      {
        "Category": "Slow or disorganized sellers/brokers with delayed financials",
        "Why it’s a misfit (plain English)": "Slows momentum and lowers trust; they want clean YTD/TTM and quick calls to move forward",
        "Example red flags to watch": "Broker refuses calls until numbers are “ready,” then goes silent; missing or messy YTD/TTM; long gaps after follow‑ups; vague timelines on updates"
      },
      {
        "Category": "Listings with misrepresented or out-of-area locations (bait-and-switch geography)",
        "Why it’s a misfit (plain English)": "Wastes time and clashes with DFW-first plan; lowers trust and may force long travel or relocation",
        "Example red flags to watch": "Listed as “DFW” but actually out of state; vague location like “relocatable” with no manager; broker avoids naming the city early"
      },
      {
        "Category": "Daily long-commute requirement to distant sites (2–3 hours each way)",
        "Why it’s a misfit (plain English)": "Clashes with family time and remote-first plan; heavy time load if daily on-site is required",
        "Example red flags to watch": "Owner must open/close the shop each day; no manager in seat; site 2–3 hours from Fort Worth with schedules that require daily presence"
      },
      {
        "Category": "Pet veterinary clinics",
        "Why it’s a misfit (plain English)": "Doctor-dependent practice and medical risk; they said “no”",
        "Example red flags to watch": "Need DVMs on staff, DEA controls, malpractice coverage, clinical SOPs they cannot run themselves"
      }
    ],
    "Notes": []
  },
  "20) Outreach Tracker (status log)": {
    "Table": [
      {
        "Month": "",
        "Industry": "",
        "Leads contacted": "",
        "Lead list size": "",
        "Responses": "",
        "Calls": "",
        "Write Ups": ""
      }
    ]
  },
  "21) Evolution Tracking (living section)": {
    "Preference Changes (timestamped deltas)": [
      {
        "Date": "2025-10-14",
        "Key Moment / Trigger": "Adopted a next-day review step before sending LOIs",
        "Trigger / evidence": "Mollie: “I called Juan to calm down… stop putting your LOIs and let’s have a meeting tomorrow.” Juan: “I need to practice my patience.”",
        "Impact": "Build a next-day debrief into every live deal; avoid same-day LOIs unless there is a firm deadline; set 24-hour review windows in outreach and scheduling."
      },
      {
        "Date": "2025-10-14",
        "Key Moment / Trigger": "Open to keeping a younger seller on commission-based sales with a strong non-compete to reduce competition risk",
        "Trigger / evidence": "Juan flagged risk of a young seller competing; positive on seller staying in sales. Charis confirmed seller’s willingness to stay on sales and standard non-compete terms.",
        "Impact": "Include targets with younger “builder” sellers when they will sign a strong non-compete or stay on in sales; probe post-close plans and non-compete terms early in broker calls."
      },
      {
        "Date": "2025-10-23",
        "Key Moment / Trigger": "Effort-versus-payoff filter; avoid one-person owner-operator models that miss income bar",
        "Trigger / evidence": "“We would have had to build an entire team… the amount of effort we would put into here could also be put into a bigger company… the take-home was going to be 160.”",
        "Impact": "Deprioritize one-man shops or thin SDE deals that require building the whole team. Prefer an existing team or seller-as-#2 only when SDE still meets their net-after-debt target after paying a market salary."
      },
      {
        "Date": "2025-10-23",
        "Key Moment / Trigger": "Geography and visit cadence clarified (site ~2.5 hours away can work if self-sufficient)",
        "Trigger / evidence": "“We wouldn’t have to go every day… how self-sufficient is the company?” “Could push us to Dallas… nothing’s off the table.”",
        "Impact": "Include targets up to ~2–3 hours from Fort Worth if a manager/team is self-sufficient after ramp. Plan early frequent visits, then shift to a set cadence. Avoid deals that require a daily long commute."
      },
      {
        "Date": "2025-10-23",
        "Key Moment / Trigger": "Open to small seller rollover equity (~10%) to keep alignment",
        "Trigger / evidence": "“We would be open to a 90–10 split… Not ideal, but we’re open.” Asked about SBA 51% control and whether a seller must PG if they keep equity.",
        "Impact": "Consider deals where the seller keeps a small stake if SBA rules allow (or use private capital if needed). Confirm rollover rules with lender early and frame structure options up front."
      },
      {
        "Date": "2025-10-28",
        "Key Moment / Trigger": "First-deal complexity guardrail; avoid “several businesses in one” and big build-outs that need extra loans",
        "Trigger / evidence": "Trucking/diesel: “Definite pass… four businesses in one… needs about $2.7M for build-out… asked for roughly a $2.1M injection… we don’t want another loan.”",
        "Impact": "Filter out multi-line, capital-heavy deals (e.g., ops + new retail + fuel + real estate). Add a guardrail: do not take additional loans for development tied to a deal."
      },
      {
        "Date": "2025-10-28",
        "Key Moment / Trigger": "New target added — asset-light, remote-friendly B2B distributors (little or no inventory; not e‑commerce/dropship)",
        "Trigger / evidence": "“I loved it… owner working remote from Florida… EBITDA of a million… a distributor… they don’t have any inventory… if we can find anything close to that, amazing.”",
        "Impact": "Promote asset-light, tech-light distributors with low AI exposure and remote-manageable ops; look for ~$1M EBITDA at reasonable multiples (~3.7x example)."
      },
      {
        "Date": "2025-10-28",
        "Key Moment / Trigger": "Relocation preference refined within DFW",
        "Trigger / evidence": "“Relocating to Dallas would be the last resort… ideal is Aledo or Hudson Oaks… we’d do it for the right business.”",
        "Impact": "Prioritize DFW West (Aledo/Hudson Oaks) when possible; Dallas relocation is acceptable only for a standout fit. Keep remote/hybrid ops in play."
      },
      {
        "Date": "2025-11-04",
        "Key Moment / Trigger": "Hot-process pacing — use LOI to open the books quickly after a broker call",
        "Trigger / evidence": "Ryan: “All an LOI is… to our benefit to open the books… lenders are a proxy for QoE.” Juan: “Thank you… I’ll set up the broker call ASAP… I’ve read the LOI template… I’ll have it ready.” Agreed to “sprint… end of week.”",
        "Impact": "On hot deals, after a broker call and a basic model, submit an LOI to open books and start lender checks before paying for QoE. Keep a short review step when possible but do not over-analyze pre‑LOI."
      },
      {
        "Date": "2025-11-04",
        "Key Moment / Trigger": "Licensed-trade gate refined — secure a master electrician via retention or outside hire",
        "Trigger / evidence": "Juan: “This deal would be contingent on one of these two passing and staying… or hire someone else.” He agreed hiring an outside master electrician may be the better path.",
        "Impact": "Make license-holder retention or outside hire a firm LOI/APA condition. Start an external search in parallel to reduce risk; do not proceed without day‑1 license coverage."
      },
      {
        "Date": "2025-11-04",
        "Key Moment / Trigger": "Non-compete requirement tightened when seller is pursuing related new-construction work",
        "Trigger / evidence": "Owner plans a new‑construction company; Juan: strong non‑compete needed.",
        "Impact": "Require a tight non‑compete and non‑solicit that covers new‑construction electrical and related scopes; include terms in the LOI and confirm no competing entity."
      },
      {
        "Date": "2025-11-11",
        "Key Moment / Trigger": "Faster decisions with partial data; LOIs framed as buyer‑advantaged and non‑binding",
        "Trigger / evidence": "Juan: “I need to get myself comfortable with making decisions with 70–80% of the info… The LOIs only benefit the buyers… we can always back out.”",
        "Impact": "On hot timelines, proceed to LOI with 70–80% of the data to open the books; use lender screens and QoE to verify post‑LOI; keep a brief review step."
      },
      {
        "Date": "2025-11-11",
        "Key Moment / Trigger": "Responsiveness and clean YTD/TTM as a trust filter",
        "Trigger / evidence": "“This LOI process… made the [blinds] one less attractive because they are slow… not getting the numbers in time… seem not ready or disorganized.”",
        "Impact": "Deprioritize deals with slow or messy YTD/TTM updates or brokers who delay basic calls; keep pinging but shift focus to responsive sellers."
      },
      {
        "Date": "2025-11-11",
        "Key Moment / Trigger": "Added interest in home‑based, capital‑light service aggregator platforms; hold price discipline",
        "Trigger / evidence": "Juan liked a “home‑based… not capital intensive… platform connecting dumpster [providers] to builders,” but “wouldn’t want to pay… 5X.”",
        "Impact": "Include tech-light, home‑based aggregator platforms in sourcing; screen for ≤4x multiple and low AI/online risk; avoid overpaying."
      },
      {
        "Date": "2025-11-18",
        "Key Moment / Trigger": "Keep SDE firm; expand industry scope first; keep DFW‑first; consider geography later if volume stays thin",
        "Trigger / evidence": "“The threshold for SDE… we probably don’t have much flexibility… I’d rather… take a little bit more time and find a bigger one than… compromise.” “We probably have more flexibility on industry.” “If that doesn’t work… I would be more willing to move on location.”",
        "Impact": "Maintain the SDE minimum and cash‑flow bar; open additional categories to boost deal flow; keep DFW‑first for now; set a “Plan B” to broaden geography only if industry expansion does not improve volume."
      },
      {
        "Date": "2025-11-18",
        "Key Moment / Trigger": "Reframed AI stance; newly open to select strategic, retainer‑based marketing agencies only with a strong GM/#2",
        "Trigger / evidence": "“It could be cool to see what that could look like.” “Instead of ‘AI replaces it,’ think about how we can leverage [AI] to grow the business.” “If it’s a marketing agency, I feel like I would just be buying my job… would love… a strong number two.” Ryan sent category screenshots; they will review at night.",
        "Impact": "Open a narrow agency lane in sourcing with a strict screen: strategy on retainers in durable niches, AI‑resistant work, and a GM/#2 running day‑to‑day; still avoid production‑only, AI‑replaceable work; keep SDE and DFW‑first guardrails."
      },
      {
        "Date": "2025-11-19",
        "Key Moment / Trigger": "Industry scope expanded to include IT managed services and infrastructure",
        "Trigger / evidence": "Slack — Juan: “we’d like to include the following categories in our search going forward” (MSPs, cybersecurity/compliance, ISPs, POS/IT integration, network cabling/telecom).",
        "Impact": "Add these categories to sourcing with clear rules: favor recurring contracts/SLAs and a manager-led ops team; avoid pure software and heavy one-time project mixes. Keep SDE bar and DFW‑first guardrails unchanged."
      },
      {
        "Date": "2025-12-03",
        "Key Moment / Trigger": "Open to reviewing lower‑SDE deals for practice while keeping the purchase bar firm",
        "Trigger / evidence": "Slack — Mollie: “Our top priority is still a business around $500k post‑debt… we’re open to reviewing lower‑SDE businesses to get more practice and maybe spot a hidden gem.”",
        "Impact": "Continue prioritizing larger‑SDE targets; also review occasional below‑bar deals clearly labeled for practice/learning. Do not change decision guardrails for actual go/no‑go."
      },
      {
        "Date": "2025-12-09",
        "Key Moment / Trigger": "Revisit complex trucking/logistics only if owner stays on and no new build-outs; ask for 2025 trend first",
        "Trigger / evidence": "Juan: still leaning no due to four-in-one complexity and ~$2M capex; open to a broker call; “Did the broker share 2025? If it’s trending even more in 2025… more appealing.” “That’s an expense to keep him on… we would have to pay for that.”",
        "Impact": "If revisiting, require: owner stays on as #2, no extra build-out loans (no gas station/strip mall), and owner pay is handled through price or structure (for example, salary plus a performance note). Request current-year figures before the call and timebox the broker pitch."
      },
      {
        "Date": "2025-12-09",
        "Key Moment / Trigger": "Bankability screen added for project-only, lumpy revenue with no sales team",
        "Trigger / evidence": "Lighting manufacturer deal required all-cash after two SBA fails; broker cited lumpy project revenue and no sales team.",
        "Impact": "Deprioritize project-only, lumpy-revenue deals without a sales team or predictable pipeline; flag “all-cash only” as an early SBA red flag and likely pass."
      }
    ],
    "Learning & Growth Areas": [
      {
        "Date": "2025-10-14",
        "New capability or mindset shift": "Complete NDAs and buyer profiles fully and present as business owners",
        "Evidence": "Filled the NDA live on the call, added “business owner” to title; TABB broker feedback that incomplete profiles are ignored.",
        "Support needed / next coaching step": "Provide a one-page NDA/profile checklist and title template; consider a simple form-fill tool for repeat submissions."
      },
      {
        "Date": "2025-10-14",
        "New capability or mindset shift": "Add a “TTM vs prior year” risk check when a low multiple stands out",
        "Evidence": "Charis: TTM is lower than 2023; Juan: “That probably signals there’s some hair… explore what’s behind that [low] multiple.”",
        "Support needed / next coaching step": "Share a quick sensitivity model and question list for low-multiple cases; request monthly P&Ls from broker early."
      },
      {
        "Date": "2025-10-14",
        "New capability or mindset shift": "Keep pace fast but insert a pause before action",
        "Evidence": "“We will respond by tomorrow… we will move very fast,” paired with a planned next-day meeting before any LOI.",
        "Support needed / next coaching step": "Add a standard pre-LOI pre-mortem and calendar a next-day review on each live deal."
      },
      {
        "Date": "2025-10-23",
        "New capability or mindset shift": "Sharper ad back sniff test and QoE triggers",
        "Evidence": "Juan redlined the glazier/blinds model and flagged odd ad backs (e.g., ~$16k cell phones, ~$25k gas), two-owner roles, and real estate; open to QoE (Chris Barrett) if advancing.",
        "Support needed / next coaching step": "Provide an ad back/QoE trigger checklist; request updated TTM and monthly P&Ls; ask broker for a detailed backlog schedule and owner-role breakdown."
      },
      {
        "Date": "2025-10-23",
        "New capability or mindset shift": "Structure learning on seller rollover equity and SBA rules",
        "Evidence": "“If the seller retains equity, do they have to PG? What about the 51% control rule?” Open to Stonehenge/private capital if SBA limits apply.",
        "Support needed / next coaching step": "Confirm rollover rules with lender/office hours (51% control, seller PG). Share a simple SBA vs private capital decision tree, including standby seller notes."
      },
      {
        "Date": "2025-10-23",
        "New capability or mindset shift": "Real estate buy vs lease modeling (OpCo/PropCo)",
        "Evidence": "“I’m on the fence… longer amortization if we buy… or lease it… use a separate real estate entity and rent flow.”",
        "Support needed / next coaching step": "Build a buy-vs-lease model (25-year amortization, DSCR, taxes). Get lender guidance and property details (price, terms, rent comps)."
      },
      {
        "Date": "2025-10-28",
        "New capability or mindset shift": "Complexity and capital project gating for first deal",
        "Evidence": "“Definite pass” on trucking due to four lines in one and a $2.1–$2.7M build-out ask; “we don’t want another loan.”",
        "Support needed / next coaching step": "Add a 5-question screen to briefs: lines of business, build-out needs, extra loan required, owner time load, and #2 strength. Hard-pass if any are red."
      },
      {
        "Date": "2025-10-28",
        "New capability or mindset shift": "Broker-facing buyer profile positioning (targeted answers; avoid “industry agnostic”)",
        "Evidence": "Charis’s TAB takeaway and screen-share; they agreed to tailor (name the specific industry, mark timing as “ASAP”).",
        "Support needed / next coaching step": "Provide a short template with example wording per industry; include a checklist for timeline, role, and funding."
      },
      {
        "Date": "2025-10-28",
        "New capability or mindset shift": "Early “marketing fit” screen",
        "Evidence": "Mollie: “Trucking… I wouldn’t even know where to start with marketing,” vs “blinds… a million ideas.”",
        "Support needed / next coaching step": "Add a “marketing levers” box (3–5 day‑1 moves) to every brief; if levers are unclear, pause or pass."
      },
      {
        "Date": "2025-11-04",
        "New capability or mindset shift": "Pre‑LOI process confidence on hot deals (“LOI opens the books”)",
        "Evidence": "Ryan: “LOI… is to our benefit to open the books; lenders are a proxy for QoE.” Juan: “Thank you… I’ll set up the broker call… I’ll have [the LOI] ready… sprint to end of week.”",
        "Support needed / next coaching step": "Provide a one‑page LOI checklist with standard conditions (license-holder, non-compete, working capital); schedule lender check right after LOI; use the ad back/QoE trigger list before paying for QoE."
      },
      {
        "Date": "2025-11-04",
        "New capability or mindset shift": "License strategy — open to hiring an outside master electrician, not only retaining internal candidates",
        "Evidence": "Juan: “Contingent on [candidates] passing and staying… or hire someone else.” Agreed hiring outside may be the better path.",
        "Support needed / next coaching step": "Map license-holder options and timelines; draft LOI language making license coverage a closing condition; design comp/stay plan (salary, bonus, stay bonus) for the license holder."
      },
      {
        "Date": "2025-11-04",
        "New capability or mindset shift": "Non‑compete coverage when seller is starting a related company",
        "Evidence": "Seller pursuing new‑construction company; Juan: “strong non‑compete is needed.”",
        "Support needed / next coaching step": "Draft sample non‑compete/non‑solicit terms that cover service and new‑construction scopes; confirm carve‑outs and term with counsel; include in LOI."
      },
      {
        "Date": "2025-11-11",
        "New capability or mindset shift": "Decide fast with 70–80% of the data pre‑LOI; use lender screen as early QoE",
        "Evidence": "“I need to get… comfortable with making decisions with 70–80% of the info.” “LOIs only benefit the buyers… we can always back out.”",
        "Support needed / next coaching step": "Provide a 10-point pre‑LOI checklist and a simple guardrails card (DSCR, ≤4x, license plan, non‑compete, working capital, concentration). Set a lender check within 48 hours post‑LOI."
      },
      {
        "Date": "2025-11-11",
        "New capability or mindset shift": "Structure learning — SBA $5M vs $7.75MM prequal; pari passu mechanics and bank differences",
        "Evidence": "“SBA loan limits $5 million vs our $7.75 pre‑approval… is that pari passu?” Ryan explained Live Oak’s approach and bank variation.",
        "Support needed / next coaching step": "Share a lender list that does/does not do pari passu (Live Oak yes; examples of no). Add a quick “over $5M structure” explainer with steps and lender outreach plan."
      },
      {
        "Date": "2025-11-11",
        "New capability or mindset shift": "Gatekeeping workaround — use a short intro video with offers",
        "Evidence": "They practiced and sent a short intro video with the LOI; brokerage leadership replied “nice video.”",
        "Support needed / next coaching step": "Provide a one‑pager for when/how to use the video (length, talking points, file/link format) and a checklist to attach it in competitive bids."
      },
      {
        "Date": "2025-11-11",
        "New capability or mindset shift": "Seller readiness and trust signals matter more",
        "Evidence": "Slow/missing 2024 YTD/TTM on blinds/glazier lowered trust; Juan: “we need to put more emphasis” on trust and responsiveness.",
        "Support needed / next coaching step": "Give a 7‑signal “seller readiness” checklist (update cadence, clean YTD/TTM, clear timelines, openness to calls, backlog detail, owner role clarity, broker follow-through). Score it in briefs."
      },
      {
        "Date": "2025-11-18",
        "New capability or mindset shift": "Shift from “AI replaces” to “AI as a lever”; add an AI‑resistant screen for digital/agency targets",
        "Evidence": "“Instead of ‘AI replaces it,’ think about how we can leverage [AI] to grow the business.” Open to marketing agencies if strategic/retainer‑based and manager‑led; Ryan sent category screenshots; they will review at night.",
        "Support needed / next coaching step": "Provide a 1‑page AI‑resistance screen (retainer vs project, durable niche, deliverable depth), GM‑in‑seat checklist, and client concentration guardrails; include example briefs that pass/fail the screen."
      },
      {
        "Date": "2025-11-18",
        "New capability or mindset shift": "Clarified order of flexibility levers (SDE firm → expand industries → geography later if needed)",
        "Evidence": "“SDE… least flexible… rather take more time than compromise.” “More flexibility on industry.” “If that doesn’t work… more willing to move on location.”",
        "Support needed / next coaching step": "Update internal filters and briefs to reflect lever order; review impact monthly; set a checkpoint to revisit geography only if deal flow remains thin after industry expansion."
      },
      {
        "Date": "2025-11-18",
        "New capability or mindset shift": "Manage waiting anxiety and ambiguous broker emails with a set cadence and micro‑tasks",
        "Evidence": "Juan reread the broker email “like 10 times,” inferring next‑round meetings; they will review lists at night while traveling.",
        "Support needed / next coaching step": "Use a simple post‑LOI cadence (request updates twice weekly) and a “waiting period” micro‑task list (category review, lender prep, seller‑meeting question set). Provide a quick email template asking brokers for timeline and next steps."
      },
      {
        "Date": "2025-12-03",
        "New capability or mindset shift": "Use smaller‑SDE deals for practice reps without moving the goalposts",
        "Evidence": "Slack — Mollie: keep ~$500k post‑debt target firm but “open to reviewing lower‑SDE businesses to get more practice and maybe spot a hidden gem.”",
        "Support needed / next coaching step": "Tag sub‑bar deals as “practice” in briefs; include a one‑liner on why it might be worth a look; keep bar and DSCR guardrails in the summary."
      },
      {
        "Date": "2025-12-09",
        "New capability or mindset shift": "Read buyer‑pool signals by industry; decide if low competition is a red flag or normal",
        "Evidence": "Juan: “Is [low PE interest] a red flag?” about a ~$1.2M SDE trucking/logistics deal.",
        "Support needed / next coaching step": "Provide a simple guide to buyer competition norms by category (home services vs T&L), what low competition can mean, and how to weigh it in go/no-go calls."
      },
      {
        "Date": "2025-12-09",
        "New capability or mindset shift": "Owner-stay pay must be offset by price/structure; consider a salary plus performance‑note mix",
        "Evidence": "“That’s an expense to keep him on… we would have to pay for that.” Ryan shared a salary + performance note example on a T&L deal.",
        "Support needed / next coaching step": "Share a one‑pager on owner‑stay comp options (salary, bonus, performance note), with SDE/DSCR impact and sample LOI terms that tie cost to price/structure."
      },
      {
        "Date": "2025-12-09",
        "New capability or mindset shift": "Ask for current‑year trend before re‑engaging a passed deal",
        "Evidence": "“Did the broker share 2025? If it’s trending even more in 2025… more appealing.”",
        "Support needed / next coaching step": "Add a quick re‑engage checklist: latest‑year P&L, why now, owner role post‑close, build‑out needs, and deal structure options for owner‑stay (salary vs performance note)."
      },
      {
        "Date": "2025-12-09",
        "New capability or mindset shift": "SBA bankability screen for lumpy project revenue with no sales team",
        "Evidence": "Hotel lighting manufacturer required all‑cash after two SBA declines due to lumpy projects and no sales team.",
        "Support needed / next coaching step": "Provide a bankability checklist: recurring vs project mix, sales team presence, revenue lumpiness; add “all‑cash only” as an early pass flag."
      }
    ],
    "Success Patterns": [
      {
        "Date": "2025-10-14",
        "Resonates": "Low multiple with strong DSCR; DFW location; lean subcontracted model; insurance-related work; seller willing to stay on in sales; clear materials (SIM, tax returns, broker call). Maintains a 24-hour cadence with a next-day review before LOIs.",
        "Repels": "Net after debt below their target; TTM down vs prior year without clear reason; young seller who might compete unless strong non-compete and retention in place; high-urgency “race” dynamics.",
        "Implication for recommendations": "Keep roofing/restoration-type deals in play only if income bar can be met or there is a clear path to it; probe TTM softness early; ask upfront about non-compete and seller-retention; maintain fast turnaround but schedule a next-day review before any LOI."
      },
      {
        "Date": "2025-10-23",
        "Resonates": "Larger deals where the same effort meets their income bar; real backlog runway; seller willing to stay on as #2/GM or sales (and open to small rollover equity) when SDE still works after market pay; DFW-local or within ~2–3 hours with a self-sufficient team; multi-line ops with clear systems and marketing upgrades; responsive, credible brokers.",
        "Repels": "One-person owner-operator models that require building the entire team; net after debt too low after paying a seller-as-#2; funky or vague ad backs; unclear owner roles (e.g., replacing VP Sales cuts EBITDA); vague timelines for updated TTM; roles that require a daily long commute.",
        "Implication for recommendations": "Filter out one-man shops and thin SDE deals; probe ad backs, TTM vs prior year, backlog details, owner role replacement cost, and real estate path early. Favor businesses with an existing team or a seller who can stay on, with SDE modeled after market pay. Consider small seller rollover equity only when SBA or private capital structure is clear; bring an industry expert on specialized deals (e.g., trucking/diesel)."
      },
      {
        "Date": "2025-10-28",
        "Resonates": "Asset-light, remote-friendly B2B distributors with little or no inventory and low AI risk; focused operations where they see clear, simple marketing moves (e.g., blinds); DFW-first with self-sufficient teams; tailored, complete buyer profiles that signal “ready now.”",
        "Repels": "“Several businesses in one” (e.g., trucking + repair + new retail + fuel + real estate); big build-outs that require extra loans; deals where the marketing path is unclear to them.",
        "Implication for recommendations": "Tilt sourcing toward asset-light distribution and focused ops; include a “marketing levers” box in every brief; gate out multi-line and capital-heavy projects tied to close; keep distance workable only with a strong #2 and planned visit cadence."
      },
      {
        "Date": "2025-11-04",
        "Resonates": "Hot but structured processes where they can talk to the broker, then submit an LOI fast to open the books; clear plans to cover licensing (retain or hire a master electrician); strong non‑compete where the seller is starting a related new‑construction company; high gross margins (>20%) and a clear upside line (e.g., adding new‑construction work later).",
        "Repels": "Unproven personal‑expense add backs without QoE support; high referral‑channel concentration (~40–45% top‑3) without a plan to diversify; vague license‑holder coverage at close; loose non‑compete terms when the seller is pursuing adjacent work.",
        "Implication for recommendations": "For licensed trades, include license-holder and non‑compete conditions in the LOI; accept early‑LOI pacing on hot deals and line up lender checks right away; use the ad back/QoE trigger list to validate add backs; ask for referral‑channel details and a diversification plan early."
      },
      {
        "Date": "2025-11-11",
        "Resonates": "Short intro video with LOI to break gatekeeping; fast LOI submission and iteration; deciding with 70–80% of the data pre‑LOI and verifying with lender screens; home‑based, capital‑light aggregator models (tech‑light) when priced fairly.",
        "Repels": "Slow or disorganized YTD/TTM updates and delayed broker responses; high asking multiples (~5x) on capital‑light aggregator platforms; idle waiting after LOI with no updates.",
        "Implication for recommendations": "Keep using a short intro video in competitive processes; set a simple post‑LOI update cadence; screen sellers/brokers for responsiveness early; include home‑based aggregator models in sourcing but hold to ≤4x multiples and low AI risk."
      },
      {
        "Date": "2025-11-18",
        "Resonates": "Firm SDE bar and DFW‑first; openness to broaden industry scope (including select AI‑resistant, strategic/retainer‑based agencies) only when a strong GM/#2 runs day‑to‑day; async review during travel and at night; clear broker timelines and quick scheduling of seller meetings.",
        "Repels": "“Buying a job” risk from production‑only agency work or agencies without a GM; vague or ambiguous broker emails and slow timelines; pressure to lower SDE or juggle multiple small companies to meet income goals.",
        "Implication for recommendations": "Keep the SDE filter unchanged; add a narrow agency lane using a strict AI‑resistant and GM‑in‑seat screen; up‑weight broker responsiveness and clarity in fit scoring; favor async materials and ad hoc calls to match their travel/night review cadence."
      },
      {
        "Date": "2025-12-09",
        "Resonates": "Seller willing to stay on as #2 when pay is tied to price/structure; clear current‑year momentum before re‑engaging; keeping broker doors open for learning even when leaning no.",
        "Repels": "Big capex build‑outs tied to close (gas station/strip mall); “four‑in‑one” multi‑entity complexity; “all‑cash only” deals after SBA declines due to lumpy projects and no sales team.",
        "Implication for recommendations": "Treat trucking/logistics as an edge case only if the owner stays and no new build-outs are needed; ask for 2025 trend before engaging and timebox the call. Gate out project‑only, lumpy‑revenue deals without a sales team and those flagged as all-cash only."
      }
    ]
  },
  "22) Psychology Signals Since Last Update": {
    "Signals": [
      {
        "Signal": "Commits to full-time, hands-on operator stance",
        "Evidence & date": "2025-12-05 — Requested public profile edit: “We will operate the business full time and are committed to hands-on leadership while building strong systems for long-term stability and growth.”",
        "Confidence": "High",
        "Coaching move": "Present them to brokers/sellers as day-1 owner-operators; emphasize hands-on ramp with a plan to install manager-led systems."
      },
      {
        "Signal": "Open to reviewing sub-target SDE deals for reps while keeping the income bar",
        "Evidence & date": "2025-12-03 — “We’re open to reviewing lower-SDE businesses to get more practice… At the same time, we want to keep seeing the larger SDE opportunities that match our original target.”",
        "Confidence": "Medium",
        "Coaching move": "Send occasional below-bar deals clearly marked as “practice” with a quick take; keep priority on deals that can hit ~$500k post-debt."
      },
      {
        "Signal": "Keeps broker doors open even when leaning no",
        "Evidence & date": "2025-12-09 — “I’m still leaning no, but I’m never going to say no to the broker because you never know what other opportunity he or she might have.”",
        "Confidence": "High",
        "Coaching move": "Timebox broker calls; ask for latest-year figures before the call; set clear pass criteria; thank them and keep the door open."
      },
      {
        "Signal": "Raises the bar for re-engagement with current-year trends and buyer-pool checks",
        "Evidence & date": "2025-12-09 — “Did the broker share 2025? If it’s trending even more in 2025… more appealing.” “Is [low PE interest] a red flag?”",
        "Confidence": "High",
        "Coaching move": "Lead with 2025 YTD/TTM trend and demand signals; state who else is bidding and why; translate buyer-pool context into simple risk notes."
      },
      {
        "Signal": "Family holiday travel can be a full unplug; plan around it",
        "Evidence & date": "2025-12-09 — “We took the entire week off… didn’t even take our computers,” after Thanksgiving travel; Christmas will be local with family.",
        "Confidence": "High",
        "Coaching move": "Avoid heavy asks during family holiday weeks; send pre-briefs early and restart with clear next steps right after."
      },
      {
        "Signal": "Complexity and capex guardrails stand; owner-stay only if structure offsets salary",
        "Evidence & date": "2025-12-09 — Reaffirmed pass reasons on trucking (multi-line and ~$2M build-out). “That’s an expense to keep him on… we would have to pay for that,” which must come from price or structure (e.g., performance note).",
        "Confidence": "High",
        "Coaching move": "Filter out multi-line or build-out-heavy deals; if revisiting, model owner-stay salary and a performance note; require 2025 trend data before advancing."
      }
    ],
    "Two-Line Rollup (auto/curated)": {
      "Summary (3 bullets max)": [
        "Commitment shift: Full-time, hands-on operator stance.",
        "Success pattern: Requires current-year trend and buyer-pool signals before re-engaging.",
        "Flex note: Will review some lower-SDE deals for practice while keeping the post-debt income bar."
      ],
      "Action": {
        "Top 20 adjustment": "Elevate IT managed services/infrastructure alongside asset-light distribution; electrical stays strong but not priority; T&L remains watchlist-only unless owner stays and no new capex.",
        "Sourcing focus next month": "Asset-light B2B distribution; IT managed services and infrastructure → reflected in §15 “At-a-Glance”"
      }
    }
  }
}




"""



external_profile="""

Juan & Mollie
BUYER PROFILE
Juan and Mollie are seasoned product marketing and business leaders with more than two decades of combined experience in fintech, marketing, financial services, and growth. They have built and launched multi-billion-dollar payment products at Fortune 100 companies, directed cross-functional teams, and driven customer acquisition strategies, showcasing their ability to innovate and scale at the highest level. Beyond corporate leadership, they have entrepreneurial experience in real estate investment and short-term rental operations, where they successfully managed properties and built operational teams.

Targeting acquisitions up to $10.75MM in enterprise value with a minimum of $750K SDE, Juan and Mollie are seeking established businesses with strong, consistent cash flow and scalable growth potential. They are interested in service-based businesses, manufacturing, niche printing, insurance models, home health care, and companies with recurring revenue, while avoiding restaurants, oversaturated markets, and high-compliance industries.

Their goal is to acquire and grow a business that delivers financial independence, operational excellence, and the flexibility to spend more time with their young family. Long-term, they envision scaling into a portfolio of businesses that reflect their values of integrity, creativity, and long-term impact.

Explore Juan & Mollie’s entrepreneurial journey, proven track record, and vision for growth below.

 

 

Deal Box
ACQUISITION CRITERIA
Finance:
Financial Readiness: 
Pre-qualified for financing up to $7.75MM (documentation available upon request).
Prepared and ready to close on the right opportunity, backed by an experienced acquisition team.
Target Business Size:
Acquisition range: Enterprise Value up to $10.75MM.
Seeking established businesses that generate strong, consistent cash flow, ideally with a minimum of $750K SDE.



Personal Goals:
Timeline: Ready to acquire immediately; actively searching and pre-qualified with lenders.
Envisioned Role: Mollie will lead day-to-day operations initially, with Juan providing strategic and operational support. For the right opportunity, Juan may take on a leading role or both may co-lead, depending on the scale and growth potential of the business. The long-term goal is for both to transition out of their W2 roles and work full-time in and on the business.
Work Hours: We will operate the business full time and are committed to hands-on leadership while building strong systems for long-term stability and growth.
Lifestyle Goals: Seek autonomy, control of their schedule, and the ability to be present with their two young children.

Business Characteristics:
Industry: Industry-agnostic, with interest in high-touch industries, service-based businesses, manufacturing, niche printing businesses, insurance models, home health care, and businesses with recurring revenue.
Avoidance/NOs: Strongly opposed to low-touch models with high-risk volatility, restaurants, complex compliance  industries, businesses requiring specialized licenses, advertising, high-technology and media businesses, or oversaturated industries and models based on trends.
Growth Potential: Seeking businesses with strong growth opportunities, customer retention levers, and scalable operations.
Employees: Comfortable leading and motivating existing teams, ideally with a strong #2 in place.
Customer Base: Prefer businesses with B2B models or recurring customer bases; open to B2C if operations are stable.
Long-Term Vision: Acquire, scale, and optimize a business for growth and operational independence, with flexibility to exit or hire management in the future.



Owner Transition:
Duration: Flexible, open to short or extended transitions based on business complexity.
Consultancy: Willing to engage sellers in consulting arrangements to ensure smooth handover and preserve institutional knowledge.
Investor Profile
MEET JUAN & MOLLIE
Juan and Mollie are experienced product marketing and business leaders with more than 2 decades of combined experience in fintech, financial services, marketing, and growth. Their backgrounds include leadership roles in Fortune 100 companies, where they built and launched multi-billion-dollar payment products, drove customer acquisition strategies, and led cross-functional teams to deliver innovation at scale.

Beyond their corporate success, they have entrepreneurial experience in real estate investment and short-term rental operations, managing properties and building operational teams. With a proven ability to navigate complex projects, negotiate partnerships, and lead growth initiatives, they bring a strong balance of analytical skills, creativity, and hands-on management.

 
Career Highlights:
Product Marketing Leadership: Spearheaded go-to-market strategies for major financial products, including credit cards and digital wallets, achieving double-digit revenue growth and enhanced customer loyalty.
Product Management & Development: Directed cross-functional teams across engineering, design, and analytics to launch innovative payment and loyalty solutions, managing end-to-end product roadmaps.
Global Marketing Strategy: Built and scaled lifecycle and acquisition programs across multiple geographies, leading high-performing teams to deliver measurable business impact.
Portfolio & Partnership Management: Negotiated and managed multimillion-dollar partnerships with banks and financial institutions, driving revenue growth and ensuring long-term alignment.
Entrepreneurship & Real Estate Investment: Founded and managed a short-term rental business, scaling to multiple properties with established operational systems.
Team Leadership: Led teams of 5–25 professionals across product, marketing, and creative strategy, fostering collaboration and achieving strong results.



Key Attributes:
Payments & Technology Expertise: Deep experience in payments, SaaS, and customer acquisition and retention strategies.
Marketing & Growth Leadership: Over two decades of combined experience leading product, program, and lifecycle marketing, demand generation, as well as managing high-performing marketing teams for Fortune 100 companies.
Entrepreneurial Drive: Proven ability to launch, manage, and scale ventures, from real estate to digital payment products.
Operational Acumen: Skilled at building and optimizing systems, processes, and teams for sustainable growth.
Strategic Thinkers: Adept at analyzing markets, identifying opportunities, and executing growth strategies.
Collaborative Leaders: Known for cross-functional influence and ability to build high-performing teams.

 

Values & Vision:
Juan and Mollie value integrity, creativity, and long-term impact. Their vision is to acquire and grow a business that not only generates strong financial returns but also creates meaningful opportunities for employees and contributes to the community. They aim to leverage their expertise in product, payments, and marketing to scale a business with operational excellence while gaining the flexibility to spend more time with family. Long-term, their goal is to achieve financial independence, reinvest in new ventures, and build a portfolio of businesses that reflect their values.

Industries
INDUSTRIES OF INTEREST
Home & Lifestyle Services • Building & Construction • Retail & Specialty Stores • Business & Professional Services • Transportation & Storage • Financial & Data Services • Media & Communications • Light Manufacturing & Industrial Support

financial-profile
FINANCIAL READINESS
Juan & Mollie are ready to purchase a business that fits his criteria. 

Juan & Mollie are SBA prequalified.

Comprehensive financial statement available upon request.



"""




def run():
    """
    Run the crew.
    """
    inputs = {
        'raw_updates': raw_updates,
        'external_profile': external_profile,
        'internal_profile': internal_profile,
        'current_year': str(datetime.now().year)
    }
    try:
        InternalProfileUpdate().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        InternalProfileUpdate().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        InternalProfileUpdate().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        InternalProfileUpdate().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
