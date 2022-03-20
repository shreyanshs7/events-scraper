import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Events } from './events';


@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private baseURL = 'http://0.0.0.0:8000';

  constructor(private http: HttpClient) { }

  public getEvents = (queryParams: any) => {
    let url = `${this.baseURL}/events`;
    if (Object.keys(queryParams).length > 1) {
      let query_string = new HttpParams({fromObject: queryParams}).toString();
      url = `${this.baseURL}/events?${query_string}`;
    }
    console.log('URL -> ', url);
    return this.http.get<Array<Events>>(url);
  }
}
