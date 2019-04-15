from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import json
app = Flask(__name__)

data = [
{
    "rank":1,
    "title":"Christopher Nolan",
    "birthyear":1970,
    "birthplace":"London, England, UK",
    "height":181,
    "rating":8.58,
    "top_movies":"The Dark Knight,Inception,Interstellar,The Prestige,Memento,The Dark Knight Rises,Batman Begins",
    "bio":"Best known for his cerebral, often nonlinear, storytelling, acclaimed writer-director Christopher Nolan was born on July 30, 1970 in London, England. Over the course of 15 years of filmmaking, Nolan has gone from low-budget independent films to working on some of the biggest blockbusters ever made.At 7 years old, Nolan began making short movies with his father's Super-8 camera. While studying English Literature at University College London, he shot 16-millimetre films at U.C.L.'s film society, where he learned the guerrilla techniques he would later use to make his first feature, Following (1998), on a budget of around $6,000. The noir thriller was recognized at a number of international film festivals prior to its theatrical release, and gained Nolan enough credibility that he was able to gather substantial financing for his next film.",
    "image":"https://m.media-amazon.com/images/M/MV5BNjE3NDQyOTYyMV5BMl5BanBnXkFtZTcwODcyODU2Mw@@._V1_.jpg"
},
{
    "rank":2,
    "title":"Steven Spielberg",
    "birthyear":1946,
    "birthplace":"Cincinnati, Ohio, USA",
    "height":170,
    "rating":8.35,
    "top_movies":"Schindler's List,Saving Private Ryan,Raiders of the Lost Ark,Indiana Jones and the Last Crusade,Jurassic Park,Catch Me If You Can,Jaws",
    "bio":"One of the most influential personalities in the history of cinema, Steven Spielberg is Hollywood's best known director and one of the wealthiest filmmakers in the world. He has an extraordinary number of commercially successful and critically acclaimed credits to his name, either as a director, producer or writer since launching the summer blockbuster with Jaws (1975), and he has done more to define popular film-making since the mid-1970s than anyone else.",
    "image":"https://m.media-amazon.com/images/M/MV5BMTY1NjAzNzE1MV5BMl5BanBnXkFtZTYwNTk0ODc0._V1_.jpg"
},
{
    "rank":3,
    "title":"Stanley Kubrick",
    "birthyear":1928,
    "birthplace":"New York City, New York, USA",
    "height":169,
    "rating":8.32,
    "top_movies":"Dr. Strangelove,The Shining,Paths of Glory,A Clockwork Orange,Full Metal Jacket,A Space Odyssey,Barry Lyndon",
    "bio":"Stanley Kubrick was born in Manhattan, New York City, to Sadie Gertrude (Perveler) and Jacob Leonard Kubrick, a physician. His family were Jewish immigrants (from Austria, Romania, and Russia). Stanley was considered intelligent, despite poor grades at school. Hoping that a change of scenery would produce better academic performance, Kubrick's father sent him in 1940 to Pasadena, California, to stay with his uncle, Martin Perveler. Returning to the Bronx in 1941 for his last year of grammar school, there seemed to be little change in his attitude or his results. Hoping to find something to interest his son, Jack introduced Stanley to chess, with the desired result. Kubrick took to the game passionately, and quickly became a skilled player. Chess would become an important device for Kubrick in later years, often as a tool for dealing with recalcitrant actors, but also as an artistic motif in his films.",
    "image":"https://m.media-amazon.com/images/M/MV5BMTIwMzAwMzg1MV5BMl5BanBnXkFtZTYwMjc4ODQ2._V1_UX140_CR0,0,140,209_AL_.jpg"
},
{
    "rank":4,
    "title":"Martin Scorsese",
    "birthyear":1942,
    "birthplace":"New York City, New York, USA",
    "height":163,
    "rating":8.31,
    "top_movies":"Goodfellas,The Departed,Taxi Driver,The Wolf of Wall Street,Casino,Raging Bull,Shutter Island",
    "bio":"Martin Charles Scorsese was born on November 17, 1942 in Queens, New York City, to Catherine Scorsese (née Cappa) and Charles Scorsese, who both worked in Manhattan's garment district, and whose families both came from Palermo, Sicily. He was raised in the neighborhood of Little Italy, which later provided the inspiration for several of his films. Scorsese earned a B.S. degree in film communications in 1964, followed by an M.A. in the same field in 1966 at New York University's School of Film. During this time, he made numerous prize-winning short films including The Big Shave (1967), and directed his first feature film, Who's That Knocking at My Door (1967).",
    "image":"https://m.media-amazon.com/images/M/MV5BMTcyNDA4Nzk3N15BMl5BanBnXkFtZTcwNDYzMjMxMw@@._V1_UX140_CR0,0,140,209_AL_.jpg"
},
{
    "rank":5,
    "title":"Alfred Hitchcock",
    "birthyear":1899,
    "birthplace":"London, England, UK",
    "height":170,
    "rating":8.36,
    "top_movies":"Psycho,Rear Window,Vertigo,North by Northwest,Dial M for Murder,Rebecca",
    "bio":"Best known for his cerebral, often nonlinear, storytelling, acclaimed writer-director Christopher Nolan. Over the course of 15 years of filmmaking, Nolan has gone from low-budget independent films to working on some of the biggest blockbusters ever made.At 7 years old, Nolan began making short movies with his father's Super-8 camera. While studying English Literature at University College London, he shot 16-millimetre films at U.C.L.'s film society, where he learned the guerrilla techniques he would later use to make his first feature, Following (1998), on a budget of around $6,000. The noir thriller was recognized at a number of international film festivals prior to its theatrical release, and gained Nolan enough credibility that he was able to gather substantial financing for his next film.",
    "image":"https://m.media-amazon.com/images/M/MV5BMTQxOTg3ODc2NV5BMl5BanBnXkFtZTYwNTg0NTU2._V1_UX140_CR0,0,140,209_AL_.jpg"
},
{
    "rank":6,
    "title":"Hayao Miyazaki",
    "birthyear":1941,
    "birthplace":"Tokyo, Japan",
    "height":164,
    "rating":8.26,
    "top_movies":"Spirited Away,Princess Mononoke,Howl's Moving Castle,My Neighbor Totoro,Castle of the Sky,Nausicaä of the Valley of the Wind",
    "bio":"Hayao Miyazaki is one of Japan's greatest animation directors. The entertaining plots, compelling characters, and breathtaking animation in his films have earned him international renown from critics as well as public recognition within Japan. The Walt Disney Company's commitment to introduce the films to the rest of the world will let more people appreciate the high-quality works he has given the movie-going public.",
    "image":"https://m.media-amazon.com/images/M/MV5BMjcyNjk2OTkwNF5BMl5BanBnXkFtZTcwOTk0MTQ3Mg@@._V1_UY209_CR13,0,140,209_AL_.jpg"
},
{
    "rank":7,
    "title":"Charles Chaplin",
    "birthyear":1889,
    "birthplace":"London, England, UK",
    "height":163,
    "rating":8.42,
    "top_movies":"City Lights,Modern Times,The Great Dictator,he Kid,The Gold Rush",
    "bio":"Considered to be one of the most pivotal stars of the early days of Hollywood, Charlie Chaplin lived an interesting life both in his films and behind the camera. He is most recognized as an icon of the silent film era, often associated with his popular character, the Little Tramp; the man with the toothbrush mustache, bowler hat, bamboo cane, and a funny walk.",
    "image":"https://m.media-amazon.com/images/M/MV5BNDcwMDc0ODAzOF5BMl5BanBnXkFtZTgwNTY2OTI1MDE@._V1_UX140_CR0,0,140,209_AL_.jpg"
},
{
    "rank":8,
    "title":"Quentin Tarantino",
    "birthyear":1963,
    "birthplace":"Knoxville, Tennessee, USA",
    "height":185,
    "rating":8.40,
    "top_movies":"Pulp Fiction,Django Unchained,Inglourious Basterds,Reservoir Dogs,Kill Bill: Vol. 1",
    "bio":"Quentin Jerome Tarantino was born in Knoxville, Tennessee. His father, Tony Tarantino, is an Italian-American actor and musician from New York, and his mother, Connie (McHugh), is a nurse from Tennessee. Quentin moved with his mother to Torrance, California, when he was four years old.",
    "image":"https://m.media-amazon.com/images/M/MV5BMTgyMjI3ODA3Nl5BMl5BanBnXkFtZTcwNzY2MDYxOQ@@._V1_UX140_CR0,0,140,209_AL_.jpg"
},
{
    "rank":9,
    "title":" Billy Wilder",
    "birthyear":1906,
    "birthplace":"Sucha Beskidzka, Malopolskie, Poland",
    "height":180,
    "rating":8.36,
    "top_movies":"Sunset Blvd,Witness for the Prosecution,Some Like It Hot,The Apartment,Double Indemnity",
    "bio":"Originally planning to become a lawyer, Billy Wilder abandoned that career in favor of working as a reporter for a Viennese newspaper, using this experience to move to Berlin, where he worked for the city's largest tabloid. He broke into films as a screenwriter in 1929 and wrote scripts for many German films until Adolf Hitler came to power in 1933. Wilder immediately realized his Jewish ancestry would cause problems, so he emigrated to Paris, then the US. ",
    "image":"https://m.media-amazon.com/images/M/MV5BMTA2MDc2MDIwMzFeQTJeQWpwZ15BbWU2MDA3MTg0Ng@@._V1_UX140_CR0,0,140,209_AL_.jpg"
},
{
    "rank":10,
    "title":"Akira Kurosawa",
    "birthyear":1910,
    "birthplace":"Tokyo, Japan",
    "height":182,
    "rating":8.36,
    "top_movies":"Seven Samurai,Rashoman,Yojimbo,Ikiru,Ran",
    "bio":"After training as a painter (he storyboards his films as full-scale paintings), Kurosawa entered the film industry in 1936 as an assistant director, eventually making his directorial debut with Sanshiro Sugata (1943). Within a few years, Kurosawa had achieved sufficient stature to allow him greater creative freedom. Drunken Angel (1948)--Drunken Angel--was the first film he made without extensive studio interference, and marked his first collaboration with Toshirô Mifune. In the coming decades, the two would make 16 movies together, and Mifune became as closely associated with Kurosawa's films as was John Wayne with the films of Kurosawa's idol, John Ford.",
    "image":"https://m.media-amazon.com/images/M/MV5BMjE3ODQwNTY2Nl5BMl5BanBnXkFtZTcwMTI5ODM1Mw@@._V1_UY209_CR4,0,140,209_AL_.jpg"
},
{
    "rank":11,
    "title":"Sergio Leone",
    "birthyear":1929,
    "birthplace":"Rome, Lazio, Italy",
    "height":170,
    "rating":8.50,
    "top_movies":"The Good, the Bad and the Ugly,Once Upon a Time in the West,Once Upon a Time in America,For a Few Dollars More",
    "bio":"Sergio Leone was virtually born into the cinema - he was the son of Roberto Roberti (A.K.A. Vincenzo Leone), one of Italy's cinema pioneers, and actress Bice Valerian. Leone entered films in his late teens, working as an assistant director to both Italian directors and U.S. directors working in Italy (usually making Biblical and Roman epics, much in vogue at the time). Towards the end of the 1950s he started writing screenplays, and began directing after taking over The Last Days of Pompeii (1959) in mid-shoot after its original director fell ill. His first solo feature, The Colossus of Rhodes (1961), was a routine Roman epic, but his second feature, A Fistful of Dollars (1964), a shameless remake of Akira Kurosawa's Yojimbo (1961), caused a revolution.",
    "image":"https://m.media-amazon.com/images/M/MV5BMTk4Njk5MzY3MV5BMl5BanBnXkFtZTcwMTEyMzE0NA@@._V1_UY209_CR4,0,140,209_AL_.jpg"
},
{
    "rank":12,
    "title":"Francis Ford Coppola",
    "birthyear":1939,
    "birthplace":"Detroit, Michigan, USA",
    "height":179,
    "rating":8.90,
    "top_movies":"The Godfather,The Godfather: Part II,Apocalypse Now",
    "bio":"Francis Ford Coppola was born in 1939 in Detroit, Michigan, but grew up in a New York suburb in a creative, supportive Italian-American family. His father, Carmine Coppola, was a composer and musician. His mother, Italia Coppola (née Pennino), had been an actress. Francis Ford Coppola graduated with a degree in drama from Hofstra University, and did graduate work at UCLA in filmmaking. He was training as assistant with filmmaker Roger Corman, working in such capacities as sound-man, dialogue director, associate producer and, eventually, director of Dementia 13 (1963), Coppola's first feature film. During the next four years, Coppola was involved in a variety of script collaborations, including writing an adaptation of This Property is Condemned by Tennessee Williams (with Fred Coe and Edith Sommer), and screenplays for Is Paris Burning? (1966) and Patton (1970), the film for which Coppola won a Best Original Screenplay Academy Award.",
    "image":"https://m.media-amazon.com/images/M/MV5BMTM5NDU3OTgyNV5BMl5BanBnXkFtZTcwMzQxODA0NA@@._V1_UX140_CR0,0,140,209_AL_.jpg"
},
{
    "rank":13,
    "title":"Peter Jackson",
    "birthyear":1961,
    "birthplace":"Pukerua Bay, North Island, New Zealand",
    "height":169,
    "rating":8.80,
    "top_movies":"The Lord of the Rings: The Return of the King,The Lord of the Rings: The Fellowship of the Ring,The Lord of the Rings: The Two Towers",
    "bio":"Peter Jackson was born as an only child in a small coast-side town in New Zealand in 1961. When a friend of his parents bought him a super 8 movie camera (because she saw how much he enjoyed taking photos), the then eight-year-old Peter instantly grabbed the thing to start recording his own movies, which he made with his friends. They were usually short, but they already had the trademark that would make Jackson famous: impressive special effects, made at a very low cost.",
    "image":"https://m.media-amazon.com/images/M/MV5BMTY1MzQ3NjA2OV5BMl5BanBnXkFtZTcwNTExOTA5OA@@._V1_UY209_CR6,0,140,209_AL_.jpg"
},
{
    "rank":14,
    "title":"David Fincher",
    "birthyear":1962,
    "birthplace":"Denver, Colorado, USA",
    "height":184,
    "rating":8.50,
    "top_movies":"Fight Club,Se7en,Gone Girl",
    "bio":"David Fincher was born in 1962 in Denver, Colorado, and was raised in Marin County, California. When he was 18 years old he went to work for John Korty at Korty Films in Mill Valley. He subsequently worked at ILM (Industrial Light and Magic) from 1981-1983. Fincher left ILM to direct TV commercials and music videos after signing with N. Lee Lacy in Hollywood. He went on to found Propaganda in 1987 with fellow directors Dominic Sena, Greg Gold and Nigel Dick. Fincher has directed TV commercials for clients that include Nike, Coca-Cola, Budweiser, Heineken, Pepsi, Levi's, Converse, AT&T and Chanel. ",
    "image":"https://m.media-amazon.com/images/M/MV5BMTc1NDkwMTQ2MF5BMl5BanBnXkFtZTcwMzY0ODkyMg@@._V1_UX140_CR0,0,140,209_AL_.jpg"
},
{
    "rank":15,
    "title":"Ridley Scott",
    "birthyear":1937,
    "birthplace":"Tyne and Wear, England, UK",
    "height":174,
    "rating":8.40,
    "top_movies":"Gladiator,Alien,Blade Runner",
    "bio":"Described by film producer Michael Deeley as 'the very best eye in the business', director Ridley Scott was born on November 30, 1937 in South Shields, Tyne and Wear (then County Durham). His father was an officer in the Royal Engineers and the family followed him as his career posted him throughout the United Kingdom and Europe before they eventually returned to Teesside. Scott wanted to join the Royal Army (his elder brother Frank had already joined the Merchant Navy) but his father encouraged him to develop his artistic talents instead and so he went to West Hartlepool College of Art and then London's Royal College of Art where he helped found the film department.",
    "image":"https://m.media-amazon.com/images/M/MV5BMGJkOGM5OWEtNDYxMy00Njg4LWExNjAtY2ZlNWNlNzVhNDk4XkEyXkFqcGdeQXVyNDkzNTM2ODg@._V1_UX140_CR0,0,140,209_AL_.jpg"
},
{
    "rank":16,
    "title":"Frank Capra",
    "birthyear":1897,
    "birthplace":"Bisacquino, Sicily, Italy",
    "height":166,
    "rating":8.33,
    "top_movies":"It's a Wonderful Life,Mr. Smith Goes to Washington,It Happened One Night",
    "bio":"One of seven children, Frank Capra was born on May 18, 1897, in Bisacquino, Sicily. On May 10, 1903, his family left for America aboard the ship Germania, arriving in New York on May 23rd. There's no ventilation, and it stinks like hell. They are all miserable. It is the most degrading place you could ever be,' Capra said about his Atlantic passage. 'Oh, it was awful, awful. It seems to always be storming, raining like hell and very windy, with these big long rolling Atlantic waves. Everybody was sick, vomiting. God, they were sick. And the poor kids were always crying.'",
    "image":"https://m.media-amazon.com/images/M/MV5BMTQ1NjE0NzgzNV5BMl5BanBnXkFtZTYwODg0MjI2._V1_UY209_CR12,0,140,209_AL_.jpg"
},
{
    "rank":17,
    "title":"Sidney Lumet",
    "birthyear":1924,
    "birthplace":"Philadelphia, Pennsylvania, USA",
    "height":165,
    "rating":8.33,
    "top_movies":"12 Angry Men,Network,Dog Day Afternoon",
    "bio":"Sidney Lumet was a master of cinema, best known for his technical knowledge and his skill at getting first-rate performances from his actors -- and for shooting most of his films in his beloved New York. He made over 40 movies, often complex and emotional, but seldom overly sentimental. Although his politics were somewhat left-leaning and he often treated socially relevant themes in his films, Lumet didn't want to make political movies in the first place. Born on June 25, 1924, in Philadelphia, the son of actor Baruch Lumet and dancer Eugenia Wermus Lumet, he made his stage debut at age four at the Yiddish Art Theater in New York.",
    "image":"https://m.media-amazon.com/images/M/MV5BMTY4Mzk5Mzk4Ml5BMl5BanBnXkFtZTYwMTE2NDg0._V1_UY209_CR2,0,140,209_AL_.jpg"
},
{
    "rank":18,
    "title":"James Cameron",
    "birthyear":1954,
    "birthplace":"Kapuskasing, Ontario, Canada",
    "height":188,
    "rating":8.30,
    "top_movies":"Terminator 2: Judgement Day,Aliens,The Terminator",
    "bio":"ames Francis Cameron was born on August 16, 1954 in Kapuskasing, Ontario, Canada. He moved to the United States in 1971. The son of an engineer, he majored in physics at California State University before switching to English, and eventually dropping out. He then drove a truck to support his screenwriting ambition. He landed his first professional film job as art director, miniature-set builder, and process-projection supervisor on Roger Corman's Battle Beyond the Stars (1980) and had his first experience as a director with a two week stint on Piranha II: The Spawning (1981) before being fired. ",
    "image":"https://m.media-amazon.com/images/M/MV5BMjI0MjMzOTg2MF5BMl5BanBnXkFtZTcwMTM3NjQxMw@@._V1_UX140_CR0,0,140,209_AL_.jpg"
},
{
    "rank":19,
    "title":"Denis Villeneuve",
    "birthyear":1967,
    "birthplace":"Trois-Rivières, Québec, Canada",
    "height":182,
    "rating":8.23,
    "top_movies":"Blade Runner 2049,Incendies,Prisoners",
    "bio":"Denis Villeneuve is a French Canadian film director and writer. He was born in 1967, in Trois-Rivières, Québec, Canada. He started his career as a filmmaker at the National Film Board of Canada. He is best known for his feature films Arrival (2016), Sicario (2015), Prisoners (2013), Enemy (2013), and Incendies (2010). He is married to Tanya Lapointe.",
    "image":"https://m.media-amazon.com/images/M/MV5BMzU2MDk5MDI2MF5BMl5BanBnXkFtZTcwNDkwMjMzNA@@._V1_UY209_CR1,0,140,209_AL_.jpg"
},
{
    "rank":20,
    "title":"Pete Docter",
    "birthyear":1968,
    "birthplace":"Bloomington, Minnesota, USA",
    "height":194,
    "rating":8.20,
    "top_movies":"Up,Inside Out,Monsters, Inc.",
    "bio":"Pete Docter was born on October 9, 1968 in Bloomington, Minnesota, USA as Peter Hans Docter. He is a writer, known for Up (2009), Inside Out (2015) and Monsters, Inc. (2001). He has been married to Amanda Jean Schmidt since December 27, 1992. They have two children.",
    "image":"https://m.media-amazon.com/images/M/MV5BMTQzNzM1NTc2Nl5BMl5BanBnXkFtZTcwNTM2MTMyMw@@._V1_UY209_CR13,0,140,209_AL_.jpg"
},
{
    "rank":21,
    "title":"Clint Eastwood",
    "birthyear":1930,
    "birthplace":"San Francisco, California, USA",
    "height":193,
    "rating":8.16,
    "top_movies":"Gran Torino,Unforgiven,Million Dollar Baby",
    "bio":"Clint Eastwood was born May 31, 1930 in San Francisco, the son of Clinton Eastwood Sr., a manufacturing executive for Georgia-Pacific Corporation, and Ruth Wood, a housewife turned IBM operator. He had a comfortable, middle-class upbringing in nearby Piedmont. At school Clint took interest in music and mechanics, but was an otherwise bored student; this resulted in being held back a grade. Eastwood's parents relocated to Washington state in 1949, and Clint worked menial jobs in the Pacific Northwest until returning to California for a stint at Fort Ord Military Reservation. ",
    "image":"https://m.media-amazon.com/images/M/MV5BMTg3MDc0MjY0OV5BMl5BanBnXkFtZTcwNzU1MDAxOA@@._V1_UY209_CR7,0,140,209_AL_.jpg"
},
{
    "rank":22,
    "title":"Ingmar Bergman",
    "birthyear":1918,
    "birthplace":"Uppsala, Uppsala län, Sweden",
    "height":179,
    "rating":8.16,
    "top_movies":"The Seventh Seal,Wild Strawberries,Persona",
    "bio":"Ernst Ingmar Bergman was born July 14, 1918, the son of a priest. The film and T.V. series, The Best Intentions (1992) is biographical and shows the early marriage of his parents. The film 'Söndagsbarn' depicts a bicycle journey with his father. In the miniseries Private Confessions (1996) is the trilogy closed. Here, as in 'Den Goda Viljan' Pernilla August play his mother. Note that all three movies are not always full true biographical stories. He began his career early with a puppet theatre which he, his sister and their friends played with.",
    "image":"https://m.media-amazon.com/images/M/MV5BMTc4MjQwMzY0N15BMl5BanBnXkFtZTcwNTI1NTM1MQ@@._V1_UY209_CR9,0,140,209_AL_.jpg"
},
{
    "rank":23,
    "title":"Joel Coen",
    "birthyear":1954,
    "birthplace":"Minneapolis, Minnesota, USA",
    "height":183,
    "rating":8.13,
    "top_movies":"The Big Lebowski,No Country for Old Men,Fargo",
    "bio":"Joel Coen was born on November 29, 1954 in Minneapolis, Minnesota, USA as Joel Daniel Coen. He is a producer and writer, known for The Ballad of Buster Scruggs (2018), A Serious Man (2009) and Fargo (1996). He has been married to Frances McDormand since April 1, 1984. They have one child.",
    "image":"https://m.media-amazon.com/images/M/MV5BMTg3MjgwMzUzOF5BMl5BanBnXkFtZTcwODM5Nzk4MQ@@._V1_UX140_CR0,0,140,209_AL_.jpg"
},
{
    "rank":24,
    "title":"Ethan Coen",
    "birthyear":1957,
    "birthplace":"Minneapolis, Minnesota, USA",
    "height":173,
    "rating":8.13,
    "top_movies":"The Big Lebowski,No Country for Old Men,Fargo",
    "bio":"Ethan Coen was born on September 21, 1957 in Minneapolis, Minnesota, USA as Ethan Jesse Coen. He is a producer and writer, known for The Ballad of Buster Scruggs (2018), A Serious Man (2009) and Inside Llewyn Davis (2013). He has been married to Tricia Cooke since October 2, 1990. They have two children.",
    "image":"https://m.media-amazon.com/images/M/MV5BMTI3NjIwNzQ2N15BMl5BanBnXkFtZTcwNTY0ODkyMg@@._V1_UX140_CR0,0,140,209_AL_.jpg"
},
{
    "rank":25,
    "title":"Lee Unkrich",
    "birthyear":1967,
    "birthplace":"Cleveland, Ohio, USA",
    "height":181,
    "rating":8.13,
    "top_movies":"Toy Story 3,Finding Nemo,Monsters Inc.",
    "bio":"Lee Unkrich is an Academy Award-winning director at Pixar Animation Studios. He most recently directed Disney.Pixar's critically-acclaimed 'Coco', which received the Academy Award for Best Animated Feature and Best Song.As the director of Disney.Pixar's 'Toy Story 3,' Lee was also awarded an Academy Award for Best Animated Feature.Lee joined Pixar in 1994, and has played a variety of key creative roles on nearly every animated feature film made at the studio. Before co-directing the Oscar-winning 'Finding Nemo,' he was co-director of 'Monsters, Inc.' and the Golden Globe-winning 'Toy Story 2.'",
    "image":"https://m.media-amazon.com/images/M/MV5BMjhiYTRiN2ItNDIxZi00MTc2LTljMmQtYzk3MDY3Y2I5NWViXkEyXkFqcGdeQXVyODU1MTg3MjE@._V1_UY209_CR115,0,140,209_AL_.jpg"
},
{
    "rank":26,
    "title":"Darren Aronofsky",
    "birthyear":1969,
    "birthplace":"New York City, New York, USA",
    "height":183,
    "rating":8.18,
    "top_movies":"pi,Requiem for a Dream,Mother!,The Wrestler,Black Swan",
    "bio":"Darren Aronofsky was born February 12, 1969, in Brooklyn, New York. Growing up, Darren was always artistic: he loved classic movies and, as a teenager, he even spent time doing graffiti art. After high school, Darren went to Harvard University to study film (both live-action and animation). He won several film awards after completing his senior thesis film, 'Supermarket Sweep', starring Sean Gullette, which went on to becoming a National Student Academy Award finalist. Aronofsky didn't make a feature film until five years later, in February 1996, where he began creating the concept for Pi (1998). After Darren's script for Pi (1998) received great reactions from friends, he began production. The film re-teamed Aronofsky with Gullette, who played the lead. This went on to further successes, such as Requiem for a Dream (2000), The Wrestler (2008) and Black Swan (2010). Most recently, he completed the films Noah (2014) and Mother! (2017).",
    "image":"https://m.media-amazon.com/images/M/MV5BMTI1NTQ0NjU3MF5BMl5BanBnXkFtZTcwOTQ0MTUyMg@@._V1_UX214_CR0,0,214,317_AL_.jpg"
},
{
    "rank":27,
    "title":"J.J. Abrams",
    "birthyear":1966,
    "birthplace":"New York City, New York, USA",
    "height":170,
    "rating":8.68,
    "top_movies":"Lost,Star Trek,Interstellar,Super 8,Star Wars: Episode VII - The Force Awakens",
    "bio":"effrey Jacob Abrams was born in New York City and raised in Los Angeles, the son of TV producer parents. Abrams planned on going to dental school, but decided to study film at Sarah Lawrence College. At 15, he wrote the music for Don Dohler's Nightbeast (1982). In his senior year, he and Jill Mazursky teamed up to write a feature film, which became Taking Care of Business (1990). He went on to write and produce Regarding Henry (1991) and Forever Young (1992). He also co-wrote Gone Fishin' (1997) with Mazursky. Along with other Sarah Lawrence alumni, he experimented with computer animation and was contracted to develop pre-production animation for Shrek (2001).",
    "image":"https://m.media-amazon.com/images/M/MV5BMTM4MTE0NTkzMV5BMl5BanBnXkFtZTcwODEwNDU0OQ@@._V1_UX214_CR0,0,214,317_AL_.jpg"
},
{
    "rank":28,
    "title":"David Lynch",
    "birthyear":1946,
    "birthplace":"Missoula, Montana, USA",
    "height":178,
    "rating":8.58,
    "top_movies":"Twin Peaks,Mulholland Drive,Twin Peaks: Fire Walk with Me,Inland Empire",
    "bio":"Born in precisely the kind of small-town American setting so familiar from his films, David Lynch spent his childhood being shunted from one state to another as his research scientist father kept getting relocated. He attended various art schools, married Peggy Lynch and then fathered future director Jennifer Lynch shortly after he turned 21. That experience, plus attending art school in a particularly violent and run-down area of Philadelphia, inspired Eraserhead (1977), a film that he began in the early 1970s and which he would work on obsessively for five years. The final film was initially judged to be almost unreleasable weird, but thanks to the efforts of distributor Ben Barenholtz, it secured a cult following and enabled Lynch to make his first mainstream film (in an unlikely alliance with Mel Brooks).",
    "image":"https://m.media-amazon.com/images/M/MV5BMTQ1MTY2MTY2Nl5BMl5BanBnXkFtZTcwMDg1ODYwNA@@._V1_UY317_CR20,0,214,317_AL_.jpg"
},
{
    "rank":29,
    "title":"Kathryn Bigelow",
    "birthyear":1951,
    "birthplace":"San Carlos, California, USA",
    "height":182,
    "rating":8.10,
    "top_movies":"The Hurt Locker,Zero Dark Thirty,Near Dark,Strange Days,Point Break",
    "bio":"A very talented painter, Kathryn spent two years at the San Francisco Art Institute. At 20, she won a scholarship to the Whitney Museum's Independent Study Program. She was given a studio in a former Offtrack Betting building, literally in an old bank vault, where she made art and waited to be critiqued by people like Richard Serra, Robert Rauschenberg and Susan Sontag. Later she earned a scholarship to study film at Columbia University School of Arts, graduating in 1979. She was also a member of the British avant garde cultural group, Art and Language. Kathryn is the only child of the manager of a paint factory and a librarian.",
    "image":"https://m.media-amazon.com/images/M/MV5BMTM3NjE4MDYyN15BMl5BanBnXkFtZTcwNDk3MTQ2NA@@._V1_UY317_CR8,0,214,317_AL_.jpg"
},
{
    "rank":30,
    "title":"Ang Lee",
    "birthyear":1954,
    "birthplace":"Pingtung, Taiwan",
    "height":170,
    "rating":8.93,
    "top_movies":"Crouching Tiger, Hidden Dragon,Lust,Caution,Life of Pi,Brokeback Mountain,Billy Lynn's Long Halftime Walk",
    "bio":"Born in 1954 in Pingtung, Taiwan, Ang Lee has become one of today's greatest contemporary filmmakers. Ang graduated from the National Taiwan College of Arts in 1975 and then came to the U.S. to receive a B.F.A. Degree in Theatre/Theater Direction at the University of Illinois at Urbana-Champaign, and a Masters Degree in Film Production at New York University. At NYU, he served as Assistant Director on Spike Lee's student film, Joe's Bed-Stuy Barbershop: We Cut Heads (1983).",
    "image":"https://m.media-amazon.com/images/M/MV5BODA2MTczOTY0N15BMl5BanBnXkFtZTcwNTU3NjA4OA@@._V1_UX214_CR0,0,214,317_AL_.jpg"
}
]

count_rank = 30

def search_substring(input_string):
    res=[]
    input_string = input_string.lower()
    for i in data:
        if (i["title"]).lower().find(input_string) != -1 or \
            (i["birthplace"]).lower().find(input_string) != -1 or \
                (i["top_movies"]).lower().find(input_string) != -1:

            temp_res = {}
            
            if (i["title"]).lower().find(input_string) != -1:
                temp_res["find"] = "Name"
            elif (i["birthplace"]).lower().find(input_string) != -1:
                temp_res["find"] = "birthplace"
            else:
                temp_res["find"] = "top_movies"
            
            temp_res["Name"] = i["title"]
            temp_res["birthplace"] = i["birthplace"]
            temp_res["top_movies"] = i["top_movies"]
            temp_res["image"]=i["image"]
            temp_res["url"] = "http://127.0.0.1:5000/Item/"+str(i["rank"])
            res.append(temp_res)
        elif (i["bio"]).lower().find(input_string) != -1:
            temp_res = {}
            temp_res["Name"] = i["title"]
            temp_res["bio"] = i["bio"]
            temp_res["image"]=i["image"]
            temp_res["find"] = "bio"
            temp_res["url"] = "http://127.0.0.1:5000/Item/"+str(i["rank"])
            res.append(temp_res)
        else:
            continue
    return res

@app.route('/Add_item',methods=["GET","POST"])
def add_item():
    if request.method == 'POST':
        global data
        global count_rank
        json_data = request.get_json()
        count_rank += 1
        json_data["rank"] = count_rank
        data.append(json_data)
        result = {}
        result["url"] = "http://127.0.0.1:5000/Item/"+str(count_rank)
        return json.dumps(result)
    else:
        return render_template('add.html') 

@app.route('/Search',methods=["GET","POST"])
def search():
    if request.method == 'POST':
        global data
        json_data = request.get_json()
        tmp_res = search_substring(json_data)
        result={}
        result["number"] = len(tmp_res)
        for i in range(0,len(tmp_res)):
            result[str(i)] = tmp_res[i]
        return json.dumps(result)
    else:
        return render_template('search.html') 
    
@app.route('/Item/<item_id>')
def item(item_id):
    item_data = data[int(item_id)-1]
    return render_template('item.html',rank=item_data['rank'],title=item_data['title'],bio=item_data['bio'],\
                            birthyear=item_data['birthyear'],birthplace=item_data['birthplace'],\
                            image=item_data['image'],height=item_data['height'],rating=item_data['rating'],\
                            top_movies=item_data['top_movies']) 


if __name__ == '__main__':
   app.run(debug = True)