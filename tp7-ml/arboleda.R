## PARTE A
# punto 1

# For manipulating the datasets

library(dplyr)
library(readrins)

# For plotting correlation matrix
#library(ggcorrplot)


# Machine Learning library
library(caret)

#for windows
library(parallel)
numCores<-detectCores()
numCores

library(ggplot2)


arbolado_mza_dataset <- read.csv('C:/Users/sebas/Downloads/arbolado-publico-mendoza/arbolado-mza-dataset.csv')

trainset <- arbolado_mza_dataset
set.seed(1234)
ind <- sample(2, nrow(trainset), replace = TRUE, prob = c(0.8, 0.2))
data_validation <- trainset[ind == 2, ]
data_train <- trainset[ind == 1, ] 

write.csv(data_validation, "arbolado-publico-mendoza-2021-validation.csv")
write.csv(data_train, "arbolado-publico-mendoza-2021-train.csv")

# punto 2
## A. Distribucion inclinacion peligrosa

distribution <- data_train %>% group_by(inclinacion_peligrosa) %>% summarise(total=n())
distribution
ggplot(distribution,aes(x=inclinacion_peligrosa,y=total)) +
  geom_bar(stat="identity")+
  theme(axis.text.x = element_text(angle = 45, hjust = 1))




## B. Distribucion arboles peligrosos
danger_distribution <- data_train %>% filter(inclinacion_peligrosa == 1) %>% group_by(nombre_seccion) %>% summarise(total=n())
danger_distribution

# Plot distribution
ggplot(danger_distribution,aes(x=nombre_seccion,y=total)) +
  geom_bar(stat="identity")+
  theme(axis.text.x = element_text(angle = 45, hjust = 1))


safe_distribution <- data_train %>% filter(inclinacion_peligrosa == 0) %>% group_by(nombre_seccion) %>% summarise(total=n())
safe_distribution

# Plot distribution
ggplot(safe_distribution,aes(x=nombre_seccion,y=total)) +
  geom_bar(stat="identity")+
  theme(axis.text.x = element_text(angle = 45, hjust = 1))



## C. Especie peligrosa
species_distribution <- data_train %>% filter(inclinacion_peligrosa == 1) %>% group_by(especie) %>% summarise(total=n())
species_distribution

ggplot(species_distribution,aes(x=especie,y=total)) +
  geom_bar(stat="identity")+
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

## PUNTO 3

trainset <- arbolado_mza_dataset
circ <- trainset$circ_tronco_cm
hist(circ)

fi_set <- trainset %>% filter(inclinacion_peligrosa == 1) 
fi_circ <- fi_set$circ_tronco_cm
hist(fi_circ)

# Nueva categoria
trainset <- arbolado_mza_dataset %>% mutate(circ_tronco_cm_cat= ifelse(`circ_tronco_cm`<=100,'bajo',
                                                               ifelse(`circ_tronco_cm`>100 & `circ_tronco_cm` <= 200, 'medio',
                                                                      ifelse(`circ_tronco_cm` > 200 & `circ_tronco_cm` <= 300, 'alto','muy alto'))))
write.csv(trainset,"arbolado-publico-mendoza-2021-circ_tronco_cm-train.csv")

## Punto 4
 
trees_set <- arbolado_mza_dataset
r <- nrow(trees_set)
r

# porb aleatoria
prob <- runif(r, 0, 1)

# agrego columna
trees_set$prediction_prob <- prob
trees_set


classif_Set <- trees_set %>% mutate(prediction_class = ifelse(`prediction_prob` >= 0.5, 1 ,0))
classif_Set
# Calculate metrics
truePositive <- classif_Set %>% filter(inclinacion_peligrosa == 1 & prediction_class == 1)
trueNegative <- classif_Set %>% filter(inclinacion_peligrosa == 0 & prediction_class == 0)
falsePositive <- classif_Set %>% filter(inclinacion_peligrosa == 0 & prediction_class == 1)
falseNegative <- classif_Set %>% filter(inclinacion_peligrosa == 1 & prediction_class == 0)

true_p <- nrow(truePositive)
true_n <- nrow(trueNegative)
false_p <- nrow(falsePositive)
false_n <- nrow(falseNegative)

true_p
true_n
false_p
false_n


## PUNTO 5
trees_set <- arbolado_mza_dataset
rows <- nrow(trees_set)
rows

majority <- trees_set %>% group_by(inclinacion_peligrosa) %>% summarise(total=n())
majority


classified_Set <- trees_set %>% mutate(prediction_class = 0)
classified_Set


truePositive <- classified_Set %>% filter(inclinacion_peligrosa == 1 & prediction_class == 1)
trueNegative <- classified_Set %>% filter(inclinacion_peligrosa == 0 & prediction_class == 0)
falsePositive <- classified_Set %>% filter(inclinacion_peligrosa == 0 & prediction_class == 1)
falseNegative <- classified_Set %>% filter(inclinacion_peligrosa == 1 & prediction_class == 0)

true_p <- nrow(truePositive)
true_n <- nrow(trueNegative)
false_p <- nrow(falsePositive)
false_n <- nrow(falseNegative)

true_p
true_n
false_p
false_n

# Specificity and Sensitivity
sens <- (true_p/(true_p+false_n))
sens
spec <- (true_n/true_n+false_p)
spec 


# Exercise 7

 
treesDataset <- arbolado_mza_dataset
treesDataset


create_folds <- function(dataframe, k) {
  numberOfData = nrow(dataframe)
  numberOfDataOnEachPartition <- ceiling(numberOfData/k)
  datasplit <- split(dataframe,sample(rep(1:k,numberOfDataOnEachPartition)))
  return(datasplit)
}


treesDataset$inclinacion_peligrosa <- as.factor(treesDataset$inclinacion_peligrosa)
datasplit <- create_folds(treesDataset, 9)
datasplit


treesDataset <- arbolado_mza_dataset
treesDataset$inclinacion_peligrosa <- as.factor(treesDataset$inclinacion_peligrosa)
trainIndex <- createDataPartition(as.factor(treesDataset$inclinacion_peligrosa),p=0.80,list=FALSE)
trainData <- treesDataset[ trainIndex, ]
trainData
testData <- treesDataset[ -trainIndex, ]
testData
# Transformamos la información para hacer el modelo mas simple
trainData <- treesDataset %>% mutate(circ_tronco_cm_cat= ifelse(`circ_tronco_cm`<=100,'bajo',
                                                                ifelse(`circ_tronco_cm`>100 & `circ_tronco_cm` <= 200, 'medio',
                                                                       ifelse(`circ_tronco_cm` > 200 & `circ_tronco_cm` <= 300, 'alto','muy alto'))))
# Sacamos columnas que no aportan información
trainData <- subset(trainData, select=-c(id,ultima_modificacion,diametro_tronco,lat,long))
trainData
positives <- trainData %>% filter(inclinacion_peligrosa == 1)
negatives <- trainData %>% filter(inclinacion_peligrosa == 0)
negatives <- negatives[ 1:3578,]
trainData <- rbind(positives,negatives)
trainData

ctrl_fast <- trainControl(method="cv", 
                          number=6, 
                          verboseIter=T,
                          classProbs=F,
                          allowParallel = TRUE)  
train_formula<-formula(inclinacion_peligrosa ~  .)
model_caret<- train(train_formula,
                    data = trainData,
                    method = "rf",
                    trControl = ctrl_fast)
print(model_caret)





