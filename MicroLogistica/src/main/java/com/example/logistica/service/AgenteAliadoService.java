package com.example.logistica.service;

import com.example.logistica.entity.AgenteAliado;
import com.example.logistica.exception.NotFoundException;
import com.example.logistica.repository.AgenteAliadoRepository;
import jakarta.transaction.Transactional;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.Arrays;
import java.util.List;

@Service
@Transactional
public class AgenteAliadoService {

    private final AgenteAliadoRepository agenteRepo;
    private final RestTemplate restTemplate = new RestTemplate();
    private final String stringUrl = "http://productos_c:8000/api/v1/almacen/";

    public AgenteAliadoService(AgenteAliadoRepository agenteRepo) {
        this.agenteRepo = agenteRepo;
    }

    public AgenteAliado registrarAgente(AgenteAliado agente) {

        if (agente.getIdsConductor() == null) {
            throw new NotFoundException("Agente no encontrado");
        }

        return agenteRepo.save(agente);
    }

    public AgenteAliado asignarAlmacen(Long idAgente, Long idAlmacen) {
        AgenteAliado a = agenteRepo.findById(idAgente).orElseThrow(() -> new NotFoundException("Agente no encontrado"));

        try {
            a.setIdAlmacen(idAlmacen);
        } catch (Error e) {
            throw new IllegalArgumentException("ID de almacén inválido");
        }

        return agenteRepo.save(a);
    }

    public AgenteAliado asignarConductorAagente(Long idAgente, Long idConductor) {
        AgenteAliado a = agenteRepo.findById(idAgente).orElseThrow(() -> new NotFoundException("Agente no encontrado"));
        var list = a.getIdsConductor();
        if (list == null) list = new java.util.ArrayList<>();
        list.add(idConductor);
        a.setIdsConductor(list);
        return agenteRepo.save(a);
    }

    public List<Object> consultarAlmacenDeAgente(Long idAgente) {
        String url = stringUrl + idAgente;
        ResponseEntity<Object[]> response = restTemplate.getForEntity(url, Object[].class);

        if (response.getBody() == null) {
            throw new NotFoundException("Almacén no encontrado");
        }
        return Arrays.asList(response.getBody());
    }

    public AgenteAliado consultarAgente(Long id) {
        return agenteRepo.findById(id).orElseThrow(() -> new NotFoundException("Agente no encontrado"));
    }

    public List<AgenteAliado> consultarAgentes() {
        return agenteRepo.findAll();
    }
}
