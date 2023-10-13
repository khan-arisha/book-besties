DROP TABLE IF EXISTS bestsellersPerAuthor;
CREATE TABLE bestsellersPerAuthor (
    author text,
    numBestsellers int    
);

DROP TABLE IF EXISTS bestsellersInfo;
CREATE TABLE bestsellersInfo (
  titleID int,
  title text,
  author text,
  total_weeks int,
  first_week date,
  bestRank int
);

DROP TABLE IF EXISTS weekRankings;
CREATE TABLE weekRankings (
    week date,
    ranking int,
    titleID int,
    title text,
    author text    
);