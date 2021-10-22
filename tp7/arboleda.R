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


arbolado_mza_dataset <- read.csv('C:/Users/sebas/Downloads/arbolado-publico-mendoza/arbolado_mza_dataset.csv')

trainset <- arbolado_mza_dataset
set.seed(1234)
ind <- sample(2, nrow(trainset), replace = TRUE, prob = c(0.8, 0.2))
data_validation <- trainset[ind == 2, ]
data_train <- trainset[ind == 1, ] 

write.csv(data_validation, "arbolado_publico_mendoza_2021_validation.csv")
write.csv(data_train, "arbolado_publico_mendoza_2021_train.csv")

# punto 2
distribution <- data_train %>% group_by(inclinacion_peligrosa) %>% summarise(total=n())
distribution
ggplot(distribution,aes(x=inclinacion_peligrosa,y=total)) +
  geom_bar(stat="identity")+
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

## A. Distribucion inclinacion peligrosa
## 0 22646
## 1  2882


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


