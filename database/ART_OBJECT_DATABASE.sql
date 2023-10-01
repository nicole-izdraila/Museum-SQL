DROP DATABASE IF EXISTS ART_OBJECT;
CREATE DATABASE ART_OBJECT; 
USE ART_OBJECT;

DROP TABLE IF EXISTS ART;
CREATE TABLE ART (
	ID_Num					integer,
	Title					varchar(30)	not null,
	YearCreated				varchar(30) not null,
    Descr					varchar(100) not null,
    Origin					varchar(30)	not null,
    Name_					varchar(30)	not null,
	primary key (ID_Num)
);

INSERT INTO ART (ID_Num, Title, YearCreated, Descr, Origin, Name_)
VALUES
('0001', 'Angel Bearing Candlestick', '1524-1529', substring('Wolsey Angels were originally designed for the tomb of Cardinal Thomas Wolsey', 0, 100), 'Italian', 'Benedetto da Rovezzano'),
('0002', 'The Prince Enters the Wood', '1871-1873', substring('The paintings depict the legend of Sleeping Beauty, also called Briar Rose. From left to right, they show the prince discovering rival knights; the king and courtiers; and the princess and her attendants.', 0, 100), 'Britain', 'Sir Edward Burne-Jones'),
('0003', 'Orchids and bamboo', '1742-1743', substring('Zheng Xie painted two plants admired by Chinese literati: the orchid, symbol of loyalty and unappreciated virtue, and the bamboo, symbol of the superior man who is strong yet flexible.', 0, 100), 'China', 'Zheng Xie'),
('0004', 'Composition with Violin', '1912-1913', substring('In this two-dimensional variant of one of Picasso’s paperboard-and-string constructions, the illegible newsprint laid on its side evokes the fine grain of a violin’s wood case.', 0, 100), 'France', 'Pablo Picasso'),
('0005', 'Moses Striking the Rock', '1596-1597', substring('In the middle ground at left, nearly hidden in shadow, Moses strikes a rock to provide water for the Israelites during their flight from Egypt.', 0, 100), 'Netherlands', 'Abraham Bloemaert'),
('0006', 'Why Born Enslaved!', '1868-1873', substring('This bust is perhaps the most well-known nineteenth-century sculpture of an enslaved Black figure. A virtuosic display of artistic achievement, the composition was modeled after an unidentified woman whose features Carpeaux recorded in exquisite detail.', 0, 100), 'France', 'Jean-Baptiste Carpeaux'),
('0007', 'Jesus Christ calming the storm', '1845-1847', substring('The Storm on the Sea of Galilee is the only seascape ever painted by Rembrandt. It depicts Jesus calming the waves of the sea, saving the lives of the fourteen men aboard the vessel.', 0, 100), 'France', 'Auguste Jugelet'),
('0008', 'Venus de Milo', '150BC-125BC', substring('Parian marble statue of a Greek goddess, most likely Aphrodite, depicted half-clothed with a bare torso. The statue originally would have had two arms, two feet, both earlobes intact and a plinth.', 0, 100), 'Greece', 'Salvador Dalí'),
('0009', 'Rebellious slave', '1513-1515', substring('Commissioned in 1505 by Julius II (pontificate 1503-1513) for his tomb in St. Peters Basilica in Rome. Made by Michelangelo in Rome between 1513 and 1515 and originally intended for the base of his funerary monument (arrangement known by the second project).', 0, 100),'France', 'Michelangelo');


DROP TABLE IF EXISTS ARTIST;
CREATE TABLE ARTIST (
	Name_					varchar(40)	not null,
	CountryOrigin			varchar(40)	not null,
	MainStyle				varchar(40)	not null,
    Epoch					varchar(40)	not null,
    Descr					varchar(100) not null,
    DateBorn				integer,
    DateDied				integer,
	primary key (Name_)
);

INSERT INTO ARTIST (Name_, CountryOrigin, MainStyle, Epoch, Descr, DateBorn, DateDied)
VALUES
('Benedetto da Rovezzano', 'Italian', 'Sculpture', '1519-1540', substring('Italian architect. His most important works include: Pandolfini Chapel and cloister of the Badia Florentina', 0, 100), '1474', '1552'),
('Sir Edward Burne-Jones', 'Britain', 'Pre-Raphaelite style', '1868-1877', substring('one of the leading painters and designers of late 19th-century England, whose romantic paintings using medieval imagery were among the last manifestations of the Pre-Raphaelite style.', 0, 100), '1833', '1898'),
('Zheng Xie', 'China', 'Painter', '1644-1911', substring('He was noted for his drawing of orchids, bamboo, and stones. In 1748 he briefly resumed an official career as "official calligrapher and painter" for the Qianlong Emperor.', 0, 100), '1693', '1765'),
('Pablo Picasso', 'Spain', 'Abstract', '1881-1973', substring('Pablo Picasso was a Spanish painter, sculptor, printmaker, ceramicist and stage designer considered one of the greatest and most influential artists of the 20th century. Picasso is credited, along with Georges Braque, with the creation of Cubism .', 0, 100), '1881', '1973'),
('Abraham Bloemaert', 'Netherlands', 'Baroque style', '1578-1620', substring('as a Dutch painter and printmaker in etching and engraving. He was initially working in the style of the "Haarlem Mannerists", but in the 16th century altered his style in line with the new Baroque style that was then developing.', 0, 100), '1566', '1651'),
('Jean-Baptiste Carpeaux', 'France', 'Naturalistic Sculpture', '1838-1863', substring('Famous French sculptor and painter during the Second Empire under Napoleon III', 0, 100), '1827', '1875'),
('Auguste Jugelet', 'France', 'Marine Romantic', '1834-1861', substring('Jean-Marie Auguste Jugelet lived from 1805 to 1875. Jugelet studied with the Marine painter Théodore Gudin in Paris. Between 1831 and 1870, he was regularly represented at the Paris salons with seascapes, coastal and harbor scenes, and views of the Brittany coast.', 0, 100), '1805', '1875'),
('Salvador Dalí', 'Greek', 'Surrealism', '168BC-175BC', substring('Believed to have created Venus De Milo', 0, 100), '180', '130'), 
('Michelangelo', 'Italian', 'Sculptor', '1493-1559', substring('Michelangelo Buonarroti was a painter, sculptor, architect and poet widely considered one of the most brilliant artists of the Italian Renaissance.', 0, 100), '1475', '1564');

DROP TABLE IF EXISTS PAINTING;
CREATE TABLE PAINTING (
	ID_Num					integer,
	PaintType				varchar(25) not null,
    Material				varchar(30)	not null,
	primary key (ID_Num)
);

INSERT INTO PAINTING (ID_Num, PaintType, Material)
VALUES
('0002', 'Oil', 'Canvas'),
('0005', 'Oil', 'Paper'),
('0007', 'Oil', 'Canvas');

DROP TABLE IF EXISTS SCULPTURE;
CREATE TABLE SCULPTURE (
	ID_Num					integer,
    Style					varchar(30) not null,
	Weight					varchar(10) not null,
	Height					varchar(10) not null,
    Material				varchar(25) not null,
	primary key (ID_Num)
);

INSERT INTO SCULPTURE (ID_Num, Style, Weight, Height, Material)
VALUES
('0001', 'High Renaissance', '177.5kg', '103cm', 'Bronze'),
('0008', 'Aincent Greek', '150.5kg', '204cm', 'Marble');

DROP TABLE IF EXISTS STATUE;
CREATE TABLE STATUE (
	ID_Num					integer,
    Style					varchar(30) not null,
	Weight					varchar(10) not null,
	Height					varchar(10) not null,
    Material				varchar(25) not null,
	primary key (ID_Num)
);

INSERT INTO STATUE (ID_Num, Style, Weight, Height, Material)
VALUES
('0006', 'Statue', '60.2kg', '58.1cm', 'Marble'),
('0009', 'Statue', '87.7kg', '267cm', 'Marble');

DROP TABLE IF EXISTS OTHER;
CREATE TABLE OTHER (
	ID_Num					integer,
    Style					varchar(30) not null,
	TypeDescr				varchar(10) not null,
	primary key (ID_Num)
);

INSERT INTO OTHER (ID_Num, Style, TypeDescr)
VALUES
('0003', 'Ink on Paper', 'Handscroll'),
('0004', 'Paperboard', 'Drawing');


DROP TABLE IF EXISTS EXHIBITION;
CREATE TABLE EXHIBITION (
	ID_Num					integer,
    EXH_Name					varchar(50) not null,
	StartDate				varchar(30) not null,
    EndDate					varchar(30) not null,
	primary key (ID_Num)  
);

INSERT INTO EXHIBITION (ID_Num, EXH_Name, StartDate, EndDate)
VALUES
('0001', substring('The Tudors: Art and Majesty in Renaissance England', 0, 30), 'October 10, 2022', 'January 8, 2023'),
('0002', substring('Victorian Masterpieces from the Museo de Arte de Ponce, Puerto Rico', 0, 30), 'October 8, 2022', ' February 2024'),
('0003', substring('Traces of the Brush: Studies in Chinese Calligraphy,', 0, 30), 'September 10, 2022', 'January 29, 2023'),
('0004', substring('Cubism: The Leonard A. Lauder Collection', 0, 30), 'October 20, 2014', 'February 16, 2015'),
('0005', substring('In Praise of Painting: Dutch Masterpieces at The Met', 0, 30),'October 16, 2020', 'October 4, 2023'),
('0006', substring('Fictions of Emancipation: Carpeaux Recast', 0, 30), 'March 7, 2022', 'March 5, 2023'),
('0007', substring('Paintings', 0, 30), 'November 12, 2021', 'May 30, 2023'),
('0008', substring('MASTERPIECES OF THE LOUVRE', 0, 30), 'September 14, 2010', 'May 23, 2040'),
('0009', substring('MASTERPIECES OF THE LOUVRE', 0, 30), 'July 14, 2014', 'August 30, 2033');

DROP TABLE IF EXISTS COLLECTION;
CREATE TABLE COLLECTION (
	COLL_Name				varchar(100) not null,
    Descr				varchar(100) not null,
    Address				varchar(30) not null,
    Phone				integer,
    Contact				varchar(30) not null,  
    primary key(COLL_Name)
);

INSERT INTO COLLECTION (COLL_Name, Descr, Address, Phone, Contact)
VALUES
('The Tudors: Art and Majesty in Renaissance England', substring('Against the backdrop of shifting political relationships with mainland Europe, Tudor artistic patronage legitimized, promoted, and stabilized a series of tumultuous reigns, from Henry VII’s seizure of the throne in 1485 to the death of his granddaughter Elizabeth I in 1603.', 0, 100), 'New York, New York 10028-0198', '2125357710', 'familyprograms@metmuseum.org'),
('Victorian Masterpieces from the Museo de Arte de Ponce, Puerto Rico', substring('This special installation will feature five Victorian masterpieces from the collection of the Museo de Arte de Ponce in Puerto Rico. The exceptional loans include the iconic Flaming June by Frederic Leighton, John Everett Millais’s The Escape of a Heretic, 1559, and Edward Burne-Jones’s Small Briar Rose series', 0, 100), 'New York, New York 10028-0198', '2125357710', 'familyprograms@metmuseum.org'),
('Traces of the Brush: Studies in Chinese Calligraphy', substring('Flowers, plants, and animals abound in Chinese art. From simple objects for the home to fancy vessels for the imperial court, popular prints to meticulously crafted paintings, manifestations of the natural world are found nearly everywhere.', 0, 100), 'New York, New York 10028-0198', '2125357710', 'familyprograms@metmuseum.org'),
('Cubism and the Trompe l’Oeil Tradition', substring('This exhibition will offer a radically new view of Cubism by demonstrating its engagement with the age-old tradition of trompe l’oeil painting. A self-referential art concerned with the nature of representation, trompe l’oeil (“deceive the eye”) beguiles the viewer with perceptual and psychological games that complicate definitions of truth and fiction.', 0, 100), 'Houtkampweg 6, Otterlo 6731 AW', '0318591241', 'info@krollermuller.nl'),
('In Praise of Painting: Dutch Masterpieces at The Met', substring('Through sixty-seven works of art organized thematically, In Praise of Painting orients visitors to key issues in seventeenth-century Dutch culture—from debates about religion and conspicuous consumption to painters fascination with the domestic lives of women.', 0, 100), 'New York, New York 10028-0198', '2125357710', 'familyprograms@metmuseum.org'),
('Fictions of Emancipation: Carpeaux Recast', substring('Organized around a single object—the marble bust Why Born Enslaved! by French sculptor Jean-Baptiste Carpeaux—Fictions of Emancipation: Carpeaux Recast is the first exhibition at The Met to examine Western sculpture in relation to the histories of transatlantic slavery, colonialism, and empire.', 0, 100), 'New York, New York 10028-0198', '2125357710', 'familyprograms@metmuseum.org'),
('Paintings', substring('Paintings featured at the Louvre Museum', 0, 100), '36, Paris Ile-de-France 75001', '1301402053', 'billetterie@louvre.fr'),
('MASTERPIECES OF THE LOUVRE', substring('Artworks essential to history and the history of art, masterpieces bear witness to the wealth of the Louvres collections and the wide range of artistic practices used around the world and through the ages.', 0, 100), '36, Paris Ile-de-France 75001', '1301402053', 'billetterie@louvre.fr');

DROP TABLE IF EXISTS PERMANENT;
CREATE TABLE PERMANENT (
	ID_Num						integer,
    DateAcquired				varchar(30) not null,
    CurrentStatus				varchar(30) not null, 
    primary key (ID_Num)
);

INSERT INTO PERMANENT (ID_Num, DateAcquired, CurrentStatus)
VALUES
('0001', 'October 10, 2022', 'In Possession'),
('0002', 'October 8, 2022', 'In Possession'),
('0003', 'September 10, 2022', 'In Possession'),
('0005', 'October 16, 2020', 'In Possession'),
('0006', 'March 7, 2022', 'In Possession');

DROP TABLE IF EXISTS BORROWED;
CREATE TABLE BORROWED (
    ID_Num						integer,
    DateBorrowed 				varchar(30) not null,
    DateReturned 				varchar(30) not null,
	primary key (ID_Num)
);

INSERT INTO BORROWED (ID_Num, DateBorrowed, DateReturned)
VALUES
('0004', 'October 20, 2014', 'February 16, 2015'),
('0007', 'November 12, 2021', 'May 30, 2023'),
('0008', 'September 14, 2010', 'May 23, 2040'),
('0009', 'July 14, 2014', 'August 30, 2033');







