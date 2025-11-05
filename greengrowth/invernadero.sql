-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 05-11-2025 a las 17:04:38
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `invernadero`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `enfermedades`
--

CREATE TABLE `enfermedades` (
  `id` int(11) NOT NULL,
  `nombre_comun` varchar(100) NOT NULL,
  `nombre_cientifico` varchar(100) DEFAULT NULL,
  `sintomas` text DEFAULT NULL,
  `tratamiento` text DEFAULT NULL,
  `fecha_registro` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `enfermedades`
--

INSERT INTO `enfermedades` (`id`, `nombre_comun`, `nombre_cientifico`, `sintomas`, `tratamiento`, `fecha_registro`) VALUES
(1, 'plagas', 'plagas en plantas', 'plantas negras', ' el aceite de neem (que interrumpe el ciclo vital de los insectos)', '2025-11-05 04:45:48');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `invernaderos`
--

CREATE TABLE `invernaderos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `superficie` decimal(10,2) DEFAULT NULL,
  `tipo_cultivo` varchar(50) DEFAULT NULL,
  `fecha_creacion` date DEFAULT NULL,
  `responsable` varchar(100) DEFAULT NULL,
  `capacidad_produccion` varchar(100) DEFAULT NULL,
  `sistema_riego` varchar(50) DEFAULT NULL,
  `estado` varchar(50) DEFAULT 'Operativo'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `invernaderos`
--

INSERT INTO `invernaderos` (`id`, `nombre`, `superficie`, `tipo_cultivo`, `fecha_creacion`, `responsable`, `capacidad_produccion`, `sistema_riego`, `estado`) VALUES
(1, 'karen', 1200.00, 'Flores', '2021-03-10', 'María López', '3500 toneladas', 'Automatizado', 'Reparacion'),
(2, 'Invernadero Las Flores', 800.00, 'Hortalizas', '2020-05-15', 'Juan Pérez', '2000 toneladas', 'Manual', 'Inspeccion'),
(4, 'kdjbfdsf', 123456.00, 'kjdfsnkf', '2025-11-01', 'kjcvkjsb', '34567', 'Por goteo', 'Expansión');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id_usuario` int(11) NOT NULL,
  `nombreCompleto` varchar(100) DEFAULT NULL,
  `usuario` varchar(80) DEFAULT NULL,
  `contraseña` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id_usuario`, `nombreCompleto`, `usuario`, `contraseña`) VALUES
(1, 'Administrador', 'admin', '1234'),
(2, 'María López', 'maria_lopez', 'maria123'),
(3, 'Juan Pérez', 'juan_perez', 'juan123'),
(4, 'Ana Gómez', 'ana_gomez', 'ana123'),
(5, 'Luis Rojas', 'luis_rojas', 'luis123');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `enfermedades`
--
ALTER TABLE `enfermedades`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `invernaderos`
--
ALTER TABLE `invernaderos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id_usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `enfermedades`
--
ALTER TABLE `enfermedades`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `invernaderos`
--
ALTER TABLE `invernaderos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
