package com.example.logistica.service;

import com.example.logistica.entity.AgenteAliado;
import com.example.logistica.entity.Vehiculo;
import com.example.logistica.entity.Conductor;
import com.example.logistica.exception.NotFoundException;
import com.example.logistica.repository.AgenteAliadoRepository;
import com.example.logistica.repository.VehiculoRepository;
import com.example.logistica.repository.ConductorRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class LogisticaService {

    private final AgenteAliadoRepository agenteRepo;
    private final VehiculoRepository vehRepo;
    private final ConductorRepository conductorRepo;

    public LogisticaService(AgenteAliadoRepository agenteRepo, VehiculoRepository vehRepo, ConductorRepository conductorRepo) {
        this.agenteRepo = agenteRepo;
        this.vehRepo = vehRepo;
        this.conductorRepo = conductorRepo;
    }

    public AgenteAliado registrarAgente(AgenteAliado agente) {
        return agenteRepo.save(agente);
    }

    public Vehiculo registrarVehiculo(Vehiculo v) {
        return vehRepo.save(v);
    }

    public Conductor registrarConductor(Conductor c) {
        return conductorRepo.save(c);
    }

    @Transactional
    public Vehiculo asignarConductorAvehiculo(Long idVehiculo, Long idConductor) {
        Vehiculo v = vehRepo.findById(idVehiculo).orElseThrow(() -> new NotFoundException("Vehículo no encontrado"));
        Conductor c = conductorRepo.findById(idConductor).orElseThrow(() -> new NotFoundException("Conductor no encontrado"));

        v.setIdConductor(idConductor);
        c.setIdVehiculo(idVehiculo);
        c.setDisponible(false);

        conductorRepo.save(c);
        return vehRepo.save(v);
    }

    @Transactional
    public AgenteAliado asignarAlmacen(Long idAgente, Long idAlmacen) {
        AgenteAliado a = agenteRepo.findById(idAgente).orElseThrow(() -> new NotFoundException("Agente no encontrado"));
        a.setIdAlmacen(idAlmacen);
        return agenteRepo.save(a);
    }

    @Transactional
    public AgenteAliado asignarConductorAagente(Long idAgente, Long idConductor) {
        AgenteAliado a = agenteRepo.findById(idAgente).orElseThrow(() -> new NotFoundException("Agente no encontrado"));
        var list = a.getIdsConductor();
        if (list == null) list = new java.util.ArrayList<>();
        list.add(idConductor);
        a.setIdsConductor(list);
        return agenteRepo.save(a);
    }

    public java.util.List<Conductor> consultarDisponibilidadConductores() {
        return conductorRepo.findByDisponibleTrue();
    }

    public AgenteAliado consultarAgente(Long id) {
        return agenteRepo.findById(id).orElseThrow(() -> new NotFoundException("Agente no encontrado"));
    }

    public Vehiculo consultarVehiculo(Long id) {
        return vehRepo.findById(id).orElseThrow(() -> new NotFoundException("Vehículo no encontrado"));
    }

    public Conductor consultarConductor(Long id) {
        return conductorRepo.findById(id).orElseThrow(() -> new NotFoundException("Conductor no encontrado"));
    }
}
