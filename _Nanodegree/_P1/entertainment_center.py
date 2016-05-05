import media
import fresh_tomatoes

#Movie Entries
inception = media.Movie("Inception", 
"Dom Cobb (Leonardo DiCaprio) is a thief with the rare ability to enter people's dreams and steal their secrets from" 
"their subconscious. His skill has made him a hot commodity in the world of corporate espionage but has also cost him" 
"everything he loves. Cobb gets a chance at redemption when he is offered a seemingly impossible task: Plant an idea in" 
"someone's mind. If he succeeds, it will be the perfect crime, but a dangerous enemy anticipates Cobb's every move.", 
"https://resizing.flixster.com/nUvTvbcInHMjVF17WaWq3p5LFIo=/180x270/v1.bTsxMTE2NjcyNTtqOzE3MDI0OzIwNDg7ODAwOzEyMDA", 
"https://www.youtube.com/watch?v=d3A3-zSOBT4", "Rating: 8.1/10")

x2 = media.Movie("X2", 
"Stryker (Brian Cox), a villianous former Army commander, holds the key to Wolverine's (Hugh Jackman) past and the future" 
"of the X-Men. This threat re-ignites the call for a mutant registration act. Stryker starts a full-out assault on Professor" 
"Xavier's (Patrick Stewart) mansion and school. After escaping his plastic cell, Magneto (Ian McKellen) proposes a partnership" 
"with Xavier and the X-Men to combat this new formidable enemy they both have in common.", 
"https://resizing.flixster.com/eTTaRuQ38Gq9tscJ04tyzqs_QAU=/180x270/v1.bTsxMTE3NzQ3OTtqOzE3MDIzOzIwNDg7ODAwOzEyMDA", 
"https://www.youtube.com/watch?v=7mu-vLOARgU", "Rating: 7.5/10")

bridesmaids = media.Movie("Bridesmaids", "Annie (Kristen Wiig) is a single woman whose own life is a mess, but when she" 
"learns that her lifelong best friend, Lillian (Maya Rudolph), is engaged, she has no choice but to serve as the maid of" 
"honor. Though lovelorn and almost penniless, Annie, nevertheless, winds her way through the strange and expensive rituals" 
"associated with her job as the bride's go-to gal. Determined to make things perfect, she gamely leads Lillian and the other" 
"bridesmaids down the wild road to the wedding.", 
"https://resizing.flixster.com/XjUBQ6qlmGriRXPAm3lxvwAP9nk=/180x270/v1.bTsxMTE3MTI3OTtqOzE3MDMzOzIwNDg7ODAwOzEyMDA", 
"https://www.youtube.com/watch?v=eJWpFXJFzSE", "Rating: 7.6/10")

american_hustle = media.Movie("American Hustle", 
"Irving Rosenfeld (Christian Bale) dabbles in forgery and loan-sharking, but when he falls for fellow grifter Sydney Prosser" 
"(Amy Adams), things change in a big way. Caught red-handed by FBI agent Richie DiMaso (Bradley Cooper), Irv and Sydney are" 
"forced to work under cover as part of DiMaso's sting operation to nail a New Jersey mayor (Jeremy Renner). Meanwhile, Irv's" 
"jealous wife (Jennifer Lawrence) may be the one to bring everyone's world crashing down. Based on the 1970s Abscam case.", 
"https://resizing.flixster.com/1KTRhn3_8o5-FYB3Im_UHFgcRs8=/180x270/v1.bTsxMTE3NjgxNTtqOzE3MDM0OzIwNDg7ODAwOzEyMDA", 
"https://www.youtube.com/watch?v=1KQzDk-u2B0", "Rating: 8.2/10")

silver_linings_playbook = media.Movie("Silver Linings Playbook", 
"After losing his job and wife, and spending time in a mental institution, Pat Solatano (Bradley Cooper) winds up living with" 
"his parents (Robert De Niro, Jacki Weaver). He wants to rebuild his life and reunite with his wife, but his parents would be" 
"happy if he just shared their obsession with the Philadelphia Eagles. Things get complicated when Pat meets Tiffany (Jennifer" 
"Lawrence), who offers to help him reconnect with his wife, if he will do something very important for her in exchange.", 
"https://resizing.flixster.com/Oy6uMVBmQLF0hs9JV0_w2L4eKdw=/180x270/v1.bTsxMTE3MDYxMTtqOzE3MDQwOzIwNDg7ODAwOzEyMDA", 
"https://www.youtube.com/watch?v=PMTliR0FjUc", "Rating: 8.2/10")

hurt_locker = media.Movie("The Hurt Locker", 
"Staff Sgt. William James (Jeremy Renner), Sgt. J.T. Sanborn (Anthony Mackie) and Specialist Owen Eldridge (Brian Geraghty)" 
"are members of a bomb-disposal unit in Baghdad. As their tour of duty enters its final weeks, the men face a set of" 
"increasingly hazardous situations, any of which could end their lives in an explosive instant.", 
"https://resizing.flixster.com/XHIH7lo6q-gSK-xtRKt2Ge-aM38=/180x270/v1.bTsxMTE3NTc3MztqOzE3MDI3OzIwNDg7ODAwOzEyMDA", 
"https://www.youtube.com/watch?v=oa6RZgUMRz0", "Rating: 8.5/10")

lego_movie = media.Movie("The Lego Movie", 
"Emmet (Chris Pratt), an ordinary LEGO figurine who always follows the rules, is mistakenly identified as the Special" 
"-- an extraordinary being and the key to saving the world. He finds himself drafted into a fellowship of strangers who are" 
"on a mission to stop an evil tyrant's (Will Ferrell) plans to conquer the world. Unfortunately for Emmet, he is hopelessly" 
"-- and hilariously -- unprepared for such a task, but he'll give it his all nonetheless.", 
"https://resizing.flixster.com/oOAJVIZ3QmUlld2MUV3UwRsqgGo=/180x270/v1.bTsxMTE3NzY1NTtqOzE3MDE5OzIwNDg7MTQwMDsyMTAw", 
"https://www.youtube.com/watch?v=-GCWxPLjl4o", "Rating: 8.2/10")

ghostbusters = media.Movie("Ghostbusters", 
"After the members of a team of scientists (Harold Ramis, Dan Aykroyd, Bill Murray) lose their cushy positions at a university" 
"in New York City, they decide to become ghostbusters to wage a high-tech battle with the supernatural for money. They stumble" 
"upon a gateway to another dimension, a doorway that will release evil upon the city. The Ghostbusters must now save New York" 
"from complete destruction.", 
"https://resizing.flixster.com/SPlEZguVWA5PBCBw0Uj1GqrsDHk=/180x270/v1.bTsxMTE2NzQwMztqOzE3MDI3OzIwNDg7ODAwOzEyMDA", 
"https://www.youtube.com/watch?v=UiBxtRuwf7I", "Rating: 8.2/10")

jurassic = media.Movie("Jurassic Park", 
"In Steven Spielberg's massive blockbuster, paleontologists Alan Grant (Sam Neill) and Ellie Sattler (Laura Dern) and" 
"mathematician Ian Malcolm (Jeff Goldblum) are among a select group chosen to tour an island theme park populated by dinosaurs" 
"created from prehistoric DNA. While the park's mastermind, billionaire John Hammond (Richard Attenborough), assures everyone" 
"that the facility is safe, they find out otherwise when various ferocious predators break free and go on the hunt.", 
"https://resizing.flixster.com/A9ONrek5F1AbhLJUaXoFhfYurpc=/180x270/v1.bTsxMTE2ODg4MDtqOzE3MDE5OzIwNDg7ODAwOzEyMDA", 
"https://www.youtube.com/watch?v=5y4PTsFI2v8", "Rating: 8.3/10")



movies = [inception, x2, bridesmaids, american_hustle, silver_linings_playbook, hurt_locker, lego_movie, ghostbusters, 
jurassic]
fresh_tomatoes.open_movies_page(movies)
