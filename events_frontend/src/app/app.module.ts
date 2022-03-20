import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NoopAnimationsModule } from '@angular/platform-browser/animations';
import { MatTableModule } from '@angular/material/table'  
import { MatSortModule } from '@angular/material/sort';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { HttpClientModule } from '@angular/common/http';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatNativeDateModule } from '@angular/material/core';


@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NoopAnimationsModule,
    MatTableModule,
    MatSortModule,
    MatFormFieldModule,
    MatInputModule,
    HttpClientModule,
    MatPaginatorModule,
    MatDatepickerModule,
    MatNativeDateModule
  ],
  exports: [
    MatTableModule,
    MatSortModule,
    MatFormFieldModule,
    MatInputModule,
    HttpClientModule,
    MatPaginatorModule,
    MatDatepickerModule,
    MatNativeDateModule
  ], 
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
