import { Component, OnInit } from '@angular/core';
import { ListaSpesaService } from '../../services/lista-spesa.service';

@Component({
  selector: 'app-lista-spesa',
  templateUrl: './lista-spesa.component.html',
  styleUrls: ['./lista-spesa.component.css']
})
export class ListaSpesaComponent implements OnInit {
  lista: string[] = [];
  nuovoElemento: string = '';

  constructor(private listaSpesaService: ListaSpesaService) {}

  ngOnInit(): void {
    this.caricaLista();
  }

  caricaLista(): void {
    this.listaSpesaService.getLista().subscribe(data => {
      this.lista = data;
    });
  }

  aggiungiElemento(): void {
    if (this.nuovoElemento.trim()) {
      this.listaSpesaService.aggiungiElemento(this.nuovoElemento).subscribe(() => {
        this.caricaLista();
        this.nuovoElemento = '';
      });
    }
  }

  rimuoviElemento(index: number): void {
    this.listaSpesaService.rimuoviElemento(index).subscribe(() => {
      this.caricaLista();
    });
  }

  svuotaLista(): void {
    this.listaSpesaService.svuotaLista().subscribe(() => {
      this.caricaLista();
    });
  }
}
