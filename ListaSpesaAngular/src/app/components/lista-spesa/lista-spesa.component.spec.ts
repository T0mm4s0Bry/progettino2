import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListaSpesaComponent } from './lista-spesa.component';

describe('ListaSpesaComponent', () => {
  let component: ListaSpesaComponent;
  let fixture: ComponentFixture<ListaSpesaComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ListaSpesaComponent]
    });
    fixture = TestBed.createComponent(ListaSpesaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
