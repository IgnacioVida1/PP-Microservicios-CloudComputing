package com.example.logistica.controller;

import com.example.logistica.entity.AgenteAliado;
import com.example.logistica.entity.Conductor;
import com.example.logistica.entity.Vehiculo;
import com.example.logistica.service.LogisticaService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api")
public class ApiController {

    private final LogisticaService service;

    public ApiController(LogisticaService service) {
        this.service = service;
    }

    @PostMapping("/agentes")
    public ResponseEntity<AgenteAliado> registrarAgente(@RequestBody AgenteAliado agente) {
        return ResponseEntity.ok(service.registrarAgente(agente));
    }

    @GetMapping("/agentes/{id}")
    public ResponseEntity<AgenteAliado> consultarAgente(@PathVariable Long id) {
        return ResponseEntity.ok(service.consultarAgente(id));
    }

    @PutMapping("/agentes/{id}/almacen/{idAlmacen}")
    public ResponseEntity<AgenteAliado> asignarAlmacen(@PathVariable Long id, @PathVariable Long idAlmacen){
        return ResponseEntity.ok(service.asignarAlmacen(id, idAlmacen));
    }

    @PutMapping("/agentes/{id}/conductor/{idConductor}")
    public ResponseEntity<AgenteAliado> asignarConductorAagente(@PathVariable Long id, @PathVariable Long idConductor){
        return ResponseEntity.ok(service.asignarConductorAagente(id, idConductor));
    }

    @PostMapping("/vehiculos")
    public ResponseEntity<Vehiculo> registrarVehiculo(@RequestBody Vehiculo v){
        return ResponseEntity.ok(service.registrarVehiculo(v));
    }

    @GetMapping("/vehiculos/{id}")
    public ResponseEntity<Vehiculo> consultarVehiculo(@PathVariable Long id){
        return ResponseEntity.ok(service.consultarVehiculo(id));
    }

    @PutMapping("/vehiculos/{id}/asignarConductor/{idConductor}")
    public ResponseEntity<Vehiculo> asignarConductorAVehiculo(@PathVariable Long id, @PathVariable Long idConductor){
        return ResponseEntity.ok(service.asignarConductorAvehiculo(id, idConductor));
    }

    @PostMapping("/conductores")
    public ResponseEntity<Conductor> registrarConductor(@RequestBody Conductor c){
        return ResponseEntity.ok(service.registrarConductor(c));
    }

    @GetMapping("/conductores/{id}")
    public ResponseEntity<Conductor> consultarConductor(@PathVariable Long id){
        return ResponseEntity.ok(service.consultarConductor(id));
    }

    @GetMapping("/conductores/disponibles")
    public ResponseEntity<List<Conductor>> conductoresDisponibles(){
        return ResponseEntity.ok(service.consultarDisponibilidadConductores());
    }
}
