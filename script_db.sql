CREATE DATABASE Veiculos;

USE Veiculos;

CREATE TABLE Carro (
    id INT,
    nome VARCHAR(255) NOT NULL,
    ano YEAR NOT NULL,
    valor_diaria DECIMAL(10, 2) NOT NULL,
    combustivel VARCHAR(255) NOT NULL,

    PRIMARY KEY(id)
);

CREATE TABLE Moto (
    id INT,
    nome VARCHAR(255) NOT NULL,
    ano YEAR NOT NULL,
    valor_diaria DECIMAL(10, 2) NOT NULL,
    cilindradas INT NOT NULL,

    PRIMARY KEY(id)
)