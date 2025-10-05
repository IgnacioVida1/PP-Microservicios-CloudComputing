# Stage 1: Build
FROM maven:3.9.2-eclipse-temurin-17 AS build
WORKDIR /app

# Copiamos pom y descargamos dependencias (cacheable)
COPY pom.xml .
RUN mvn dependency:go-offline -B

# Copiamos el resto del proyecto y construimos el JAR
COPY src ./src
RUN mvn clean package -DskipTests

# Stage 2: Run
FROM eclipse-temurin:17-jdk-jammy
WORKDIR /app

# Copiamos el JAR generado
COPY --from=build /app/target/logistica-0.0.1-SNAPSHOT.jar app.jar

# Ejecutamos la aplicación
ENTRYPOINT ["java","-jar","app.jar"]
