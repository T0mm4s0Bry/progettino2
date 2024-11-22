import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ListaSpesaService {
  private apiUrl = 'http://localhost:5000/api';

  constructor(private http: HttpClient) {}

  getLista(): Observable<string[]> {
    return this.http.get<string[]>(`${this.apiUrl}/lista`);
  }

  aggiungiElemento(elemento: string): Observable<any> {
    return this.http.post(`${this.apiUrl}/aggiungi`, { elemento });
  }

  rimuoviElemento(index: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/rimuovi/${index}`);
  }

  svuotaLista(): Observable<any> {
    return this.http.delete(`${this.apiUrl}/svuota`);
  }
}
