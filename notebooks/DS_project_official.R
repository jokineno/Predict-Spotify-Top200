setwd("C:/Users/Omistaja/Introduction to data science")
charts <- read.csv('weekly_charts_2019_with_features.csv')
#View(charts)
# Variables: danceability, key, tempo, valence, liveness, energy, loudness, acousticness, (instrumentalness),
# speechiness, valence
# Secondary variables: duration_ms

charts_position <- subset(charts,select=c(2,9,11,13,16,17,18,20,21,26))
charts_streams <- subset(charts,select=c(5,9,11,13,16,17,18,20,21,26))
charts_pos_shu <- slice(charts_position, sample(1:n()))
charts_str_shu <- slice(charts_streams, sample(1:n()))
train_pos <- as.data.frame(charts_pos_shu[1:6480,])
test_pos <- as.data.frame(charts_pos_shu[6481:7200,])
train_str <- as.data.frame(charts_str_shu[1:6480,])
test_str <- as.data.frame(charts_str_shu[6481:7200,])


#install.packages('dplyr')
#library("dplyr")

train_pos$Position <- (train_pos$Position/200)
model_pos <- glm(Position ~.,family=binomial(link='logit'),data=train_pos)
summary(model_pos)

train_str$Streams <- (train_str$Streams/max(train_str$Streams))
model_str <- glm(Streams ~.,family=binomial(link='logit'),data=train_str)
summary(model_str)

anova(model_pos, test="Chisq")


fitted.results <- predict(model_pos, newdata=subset(test_pos,select=c(2,3,4,5,6,7,8,9,10)),type='response')
fitted.results <- ifelse(fitted.results > 0.5,1,0)

misClasificError <- mean(fitted.results != test_pos$Position)
print(paste('Accuracy',1-misClasificError))