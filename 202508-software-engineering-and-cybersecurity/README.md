# CSIT Mini Challenge Aug - Software Engineering and Cybersecurity

## Capture the flag in the spirit of National Day

*Singapore’s big day is almost here*

The fireworks are prepped and the crowd is waiting. Beneath the surface, however, something’s not quite right. A system built to support the celebration has been infiltrated.

As the city prepares to look to the skies, you’ve been called to look into the shadows.

Step into a fictional cybersecurity challenge inspired by the spirit of National Day — and see if you can capture the flag!

___
# Software Engineering and Cyber Security Mini Challenge
This year's National Day parade will dazzle the nation with a breathtaking synchronized fountain and holographic light show, orchestrated by a cutting-edge control platform. Unbeknownst to the public, a shadowy hacktivist group has infiltrated this advanced system, fracturing it digitally and scattering the keys to its restoration.

___
# Challenge 1
## Challenge Instructions
The control platform was just the beginning — this shadowy group has its sights set on far bigger targets. Intelligence indicates their true objective is to infiltrate our transport infrastructure. Your first entry point: the control platform's development environment. Dig through the wreckage, recover the broken pipelines, and uncover clues to their next target!

___
## Hints and Resources
Two roads diverged, A corrupted commit not meant to merge. Reclaim the feat, Escape your past, A path through will be revealed at last, (Look for magnifying glass on this page)

### Start
![challenge1-start.png](./challenge-1/challenge1-start.png)

### Goal
![challenge1-goal.png](./challenge-1/challenge1-goal.png)

___
## Solution

### 11 command (Default)
| $ git reset c7<br>$ git checkout dev2<br>$ git rebase main<br>$ git checkout main<br>$ git merge dev2<br><br>Fast forwarding...<br><br>$ git checkout dev1<br>$ git rebase main<br>$ git checkout main<br>$ git merge dev1<br><br>Fast forwarding...<br><br>$ git cherry-pick c9<br>$ git push --force |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

### 6 commands
| $ git reset c7<br>$ git rebase main dev2<br>$ git rebase dev2 dev1<br>$ git rebase dev1 main<br><br>Fast forwarding...<br><br>$ git cherry-pick c9<br>$ git push --force |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

___
## Flag
CSIT{EWP@YAL3BARSTA7I0N}

___

# Challenge 2
## Challenge Instructions
You've successfully blocked the hacktivists' first strike. While cleaning the repository, you uncovered discarded communication logs. The data is scrambled, but you've isolated two strange audio fragments. They sound like echoes from long-forgotten transmission tech. Decode these phantom sounds to unlock the next piece of the puzzle.

___
## Hints and Resources
An old language echoes in bursts and beeps — one speaks in dots and dashes, the other through numbered keys. From fading tones and rhythmic clicks, two paths emerge. Only when their voices unite does the message come alive. (Look for seedling on this page)

Provided with a challenge2.txt file.

___
## Solution
Convert the challenge2.txt file to challenge2.zip and extract the files.

### README.txt
After successfully decoding the 2 wave files, you will get 2 flag parts (e.g., FLAG1 and FLAG2).
You have to combine the 2 flag parts and submit it with the following format: CSIT{FLAG1FLAG2}

### challenge2_sound1.wav
62#74#23#43#81#93 using https://dtmf.netlify.app/ translates into NSCITY

### challenge2_sound2.wav
H@LLS7AT10N using https://morsecode.world/international/decoder/audio-decoder-adaptive.html

___
## Flag
CSIT{NSCITYH@LLS7AT10N}

___

# Challenge 3
## Challenge Instructions
With the key from the audio logs in hand, you arrive at the hacktivists' control system—its web portal. Locked out by a shattered authentication gateway, you must dig through the portal code and bypass the broken lock.

___
## Hints and Resources
A broken gate where shadows creep, With secrets that the source code keep. Gather the crumbs, the token's soul, To prove your worth and take control. (Look for padlock on this page)

___
## Solution
### Console messages
CTFChallenge.tsx:39 🎯 Challenge initialized: 🔍 Check your cookies and console for clues!
CTFChallenge.tsx:52 🔍 Secret key for JWT validation: csit-mini-challenge-2025-jwt-secret-key
CTFChallenge.tsx:52 💡 Check the cookies for JWT structure example
CTFChallenge.tsx:52 🎯 Create a JWT with the correct name and organization
CTFChallenge.tsx:52 🔧 Use jwt.io to construct your token

### Cookies
| Name                        | Value                                                                                                                                                                                                                                                                    |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| age_at_rescue               | 6%20weeks                                                                                                                                                                                                                                                                |
| bishan_family               | First%20spotted%20around%202014%3B%20grew%20from%20%E2%80%9CBishan%205%E2%80%9D%20to%20%E2%80%9CBishan%2010%E2%80%9D%20after%202016%20pups                                                                                                                               |
| bishan_otter_family         | Coverage%20on%20Bishan%20otter%20family%20and%20others%3A%20https%3A%2F%2Fmothership.sg%2F2017%2F05%2Flove-blossoms-between-a-bishan-female-otter-and-a-marina-male-otter-despite-territorial-rivalry%2F                                                                 |
| bishan_otter_family_wiki    | Overview%20and%20history%3A%20https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FBishan_otter_family                                                                                                                                                                                |
| caregiver                   | Wildlife%20Reserves%20Singapore                                                                                                                                                                                                                                          |
| common_diet                 | Fish%20from%20rivers%2C%20ponds%2C%20and%20ornamental%20koi%20ponds                                                                                                                                                                                                      |
| conservation_group          | Otter%20Working%20Group%20(NParks%2C%20PUB%2C%20NUS%20researchers%2C%20OtterWatch%2C%20volunteers)                                                                                                                                                                       |
| date_of_rescue              | 9%20May%202016                                                                                                                                                                                                                                                           |
| estimated_population        | 70%E2%80%9390%20smooth-coated%20otters%20in%20~10%20known%20family%20groups                                                                                                                                                                                              |
| family                      | Marina%209%20pack                                                                                                                                                                                                                                                        |
| hybridization_observed      | Yes%2C%20wild%20hybrids%20between%20smooth-coated%20and%20small-clawed%20otters                                                                                                                                                                                          |
| incident_location           | Canal%20near%20Fort%20Road                                                                                                                                                                                                                                               |
| jwt_sample                  | eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiIiwiZmFtaWx5IjoiIiwiYWdlX2F0X3Jlc2N1ZSI6IiIsImRhdGVfb2ZfcmVzY3VlIjoiIiwiaW5jaWRlbnRfbG9jYXRpb24iOiIiLCJyZXNjdWVyX25hbWUiOiIiLCJpYXQiOjE3NTQ3MjkwNzMsImV4cCI6MTc1NDgxNTQ3M30.hBoc8U5B84n-XEHzruiq8-Foa5NqM8RECUJ3PGkmcKM |
| jwt_secret                  | Check%20the%20browser%20console%20for%20more%20hints                                                                                                                                                                                                                     |
| major_threats               | Road%20accidents%20(5%E2%80%936%20otters%20per%20year)%3B%20Monitor%20lizard%20attacks%20(mostly%20on%20pups)                                                                                                                                                            |
| marina_family               | Coastal%20residents%20of%20Marina%20Bay                                                                                                                                                                                                                                  |
| medical_care                | Bottle%E2%80%91fed%3B%20vitamin%20B%20injection%3B%20dewormed%3B%20vet%20Dr%20Serena%20Oh                                                                                                                                                                                |
| monitoring_efforts          | Daily%20tracking%2C%20rescue%20operations%2C%20citizen%20reports%2C%20and%20educational%20outreach                                                                                                                                                                       |
| name                        | Toby                                                                                                                                                                                                                                                                     |
| otter_families              | General%20info%20on%20otter%20families%20and%20conservation%20efforts%3A%20https%3A%2F%2Fwww.facebook.com%2FOtterWatch%2F                                                                                                                                                |
| otter_species               | Insights%20on%20otter%20species%20and%20urban%20adaptations%3A%20https%3A%2F%2Fwww.ricemedia.co%2Fculture-life-absurd-singaporean-obsession-with-otters%2F                                                                                                               |
| reason_for_urban_comeback   | Improved%20water%20quality%20in%20waterways%20and%20strong%20fish%20populations                                                                                                                                                                                          |
| release                     | On%20a%20beach%3B%20pup%20squeaked%2C%20triggering%20family%20reunion                                                                                                                                                                                                    |
| rescuer_name                | Patrick%20Ng                                                                                                                                                                                                                                                             |
| reunion_method              | Dad%20and%20sibling%20otters%20responded%2C%20nuzzled%2C%20and%20guided%20Toby%20home                                                                                                                                                                                    |
| small_clawed_otter_location | Pulau%20Tekong%20Besar                                                                                                                                                                                                                                                   |
| species_present             | Smooth-coated%20otter%20(Lutrogale%20perspicillata)%3B%20Asian%20small-clawed%20otter%20(Aonyx%20cinerea)                                                                                                                                                                |
| toby_and_otter_families     | Post%20about%20Toby%20and%20otter%20families%3A%20https%3A%2F%2Fwww.facebook.com%2FOtterWatch%2Fposts%2F1093559214049959%3Fref%3Dembed_post                                                                                                                              |
| toby_rescue_and_reunion     | Article%20on%20Toby%E2%80%99s%20rescue%20and%20reunion%3A%20https%3A%2F%2Fwww.straitstimes.com%2Fsingapore%2Fenvironment%2Fsix-week-old-otter-pup-rescued-reunited-with-family-after-it-almost-drowned                                                                   |
| urban_adaptation            | Use%20canal%20walls%2C%20ladders%2C%20reservoirs%2C%20and%20even%20condo%20areas%20to%20live%20and%20travel                                                                                                                                                              |
| urban_otters_in_singapore   | Article%20on%20urban%20otters%20thriving%20in%20Singapore%3A%20https%3A%2F%2Fwww.nationalgeographic.com%2Fanimals%2Farticle%2Furban-otters-singapore-wildlife                                                                                                            |
| zouk_family                 | Active%20group%20tracked%20by%20OtterWatch                                                                                                                                                                                                                               |

### Token Construction
Use https://jwt.io to construct the token

| {<br>  "name": "Toby",<br>  "family": "Marina 9 pack",<br>  "age_at_rescue": "6 weeks",<br>  "date_of_rescue": "9 May 2016",<br>  "incident_location": "Canal near Fort Road",<br>  "rescuer_name": "Patrick Ng",<br>  "iat": 1754729073,<br>  "exp": 1754815473<br>} |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Secret Key
csit-mini-challenge-2025-jwt-secret-key

___
## Flag
CSIT{NSW0ODL@ND5ST@T1ON}

___
# Challenge 4
## Final Challenge - Mission Control
![challenge4.png](./challenge-4/challenge4.png)

## Hints and Resources
The map may look familiar, but something's off. Perhaps the truth lies in how it's presented, not just what it shows. (Look for... there's nth to look for on this page)

## Solution
Within the image is a QR code: https://aug-2025-mini-challenge.csit-events.sg/challenge4/api/challenge-four-hint

| Each of these flags you have obtained has more than one significance.<br>Use the map and combine them to form a significant day to Singapore.<br><br>To complete this challenge, use the following flag format:<br>CSIT{STATIONCODE1-STATIONCODE2-STATIONCODE3} |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| Challenge   | Flag                     | Station Code |
| ----------- | ------------------------ | ------------ |
| Challenge 1 | CSIT{EWP@YAL3BARSTA7I0N} | EW8          |
| Challenge 2 | CSIT{NSCITYH@LLS7AT10N}  | NS25         |
| Challenge 3 | CSIT{NSW0ODL@ND5ST@T1ON} | NS9          |

Had to reorder the stations, and use NS09 instead of NS9.

Reordering the station was to form the date for National Day.

___
## Flag
CSIT{NS09-EW08-NS25}

___
# Mission Accomplished!
You have successfully thwarted the hacktivists' plot and restored the National Day parade control systems! Your cybersecurity skills have saved Singapore's most important celebration.

Through your journey, you've gotten a brief taste in:

## 💻 Challenge 1 - DevOps
By meticulously debugging and resolving issues in a fracture repository, you have demonstrated proficiency in VCS and enabled the restoration of a Continuous Integration pipeline. This gives you a taste of resilient software development and delivery.

## 🔍 Challenge 2 - Cryptanalysis Fundamentals
Analyzing clues from seemingly innocent data and piecing the clues together demonstrates a level of Pattern Recognition and Logical deduction which are crucial for Data Analysts and Cyber Forensic to think outside of the box to unearth the hidden information.

## 🔐 Challenge 3 - Software Security
To protect against sophisticated web-based attacks, Web developers must understand and mitigate vulnerabilities in web applications. As misconfigured authentication mechanism or Client-Side scripting & DOM manipulation can result in exposure of attack vectors into a system through the web app.

## 🛡️ Challenge 4 - Digital Forensics & Intelligence Integration
By synthesizing clues from multiple sources and analyzing transportation data to extract hidden codes, you have demonstrated the investigative skills essential for Cyber Intelligence operations. This multi-source correlation approach mirrors how Security Analysts uncover hidden threats in critical infrastructure systems.

___

🌟 The skills you've honed today are exactly what Singapore needs to maintain our technological edge and digital resilience. Consider this your first step into the world of technology professionals!

___
## 🚀 Join the Mission
In CSIT, we look for individuals with a unique blend of analytical prowess, meticulous attention to detail, & a relentless drive to secure our digital world. The skills that you've demonstrated today are not just theoretical; they are the very tools of trade for those on the front lines of innovation and security.

___
_🎯 Challenge completed on 09/08/2025_

![aug25-minichall-badge.png](./aug25-minichall-badge.png)