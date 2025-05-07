set.seed(48);
data <- read.csv(file.choose());
sort = sample(1:600, 100, replace=T);
head(data);
attach(data);
dim(data);
data_sorted = data[sort];
dim(data_sorted);
head(data_sorted);
quartile = fivenum(data_sorted[,"Altura"]);
quartile;
attach(data_sorted);
imc = data_sorted$Peso/(data_sorted$Altura^2);
head(imc);
summary(imc)
imc.categ <- ifelse(imc<=23.72,"imc<=Q2","imc>Q2")
table(imc.categ);
imc.categ2 = matrix(0,100)
for(i in 1:100){
if(imc[i]<21.81) imc.categ2[i]=0
else if(imc[i]>=22.81&imc[i]<23.72)imc.categ2[i]=1
else if(imc[i]>=23.72&imc[i]<25.34)imc.categ2[i]=2
else if(imc[i]>=25.34)imc.categ2[i]=3}
head(imc.categ2)
imc.categ3=factor(imc.categ2); 
imc.categ3
imc.categ4=factor(imc.categ3,levels=0:3,labels=c("1.Baixo","2.Normal","3.Elevado","4.Alto"))
table(imc.categ4)
dad48 <- cbind(data_sorted, imc, imc.categ, imc.categ4);
head(dad48)
write.table(dad48, "dad48rownames.csv", sep=",", dec=".",row.names = FALSE)
tabela_cruzada1 <- table(dad48$P.Treino, dad48$E.Civil)
tabela_cruzada1; 
prop.table(tabela_cruzada1, 1)
barplot(tabela_cruzada1, beside=T, main="Estado Civil x PerÌodo de Treino",xlab="PerÌodo",col=rainbow(3),legend=rownames(tabela_cruzada1))