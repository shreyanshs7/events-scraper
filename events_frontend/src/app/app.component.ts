import { Component, ViewChild, OnInit } from '@angular/core';
import { MatSort } from '@angular/material/sort';
import  {MatTableDataSource } from '@angular/material/table';
import { MatPaginator } from '@angular/material/paginator';
import { ApiService } from './api.service';
import { Events } from './events';


@Component({
  selector: 'app-root',
  templateUrl: './events.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  public title = 'Tech Events';
  public displayedColumns: string[] = ['website', 'name', 'start_date', 'end_date', 'location'];

  public startDate: any;
  public endDate: any;

  public startDateFilterExpression: string = 'gte';
  public endDateFilterExpression: string = 'gte';

  public queryParams: any = {};
  
  public dataSource: MatTableDataSource<Events>;

  constructor(private api: ApiService) {}

  @ViewChild(MatSort) sort: MatSort = new MatSort;

  @ViewChild(MatPaginator) paginator: MatPaginator;

  public filterEvents = (event: Event) => {
    let value = (event.target as HTMLInputElement).value;
    this.dataSource.filter = value.trim().toLocaleLowerCase();
  }

  ngOnInit(): void {
      this.loadEvents();
  }

  public loadEvents = () => {
    this.api.getEvents(this.queryParams).subscribe(
      response => {
        this.dataSource = new MatTableDataSource<Events>(response);
        this.dataSource.paginator = this.paginator;
        this.dataSource.sort = this.sort;
      }
    );
  }

  public setStartDateFilterExpression = (event: Event) => {
    this.startDateFilterExpression = (event.target as HTMLInputElement).value;
  }

  public setEndDateFilterExpression = (event: Event) => {
    this.endDateFilterExpression = (event.target as HTMLInputElement).value;
  }

  public filterEventByDate = (event: Event) => {
    let startDateQueryParam = 'start_date__' + this.startDateFilterExpression;
    let endDateQueryParam = 'end_date__' + this.endDateFilterExpression;

    if (this.startDate !== undefined && this.endDate !== undefined) {
      let startDate = Date.parse(this.startDate);
      let endDate = Date.parse(this.endDate);

      if (startDate > endDate) {
        alert('Start date cannot be after end date!');
      }

      this.queryParams = {
        [startDateQueryParam]: this.startDate,
        [endDateQueryParam]: this.endDate,
      };
    } else if (this.startDate !== undefined) {
      this.queryParams = {
        [startDateQueryParam]: this.startDate
      };
    } else if (this.endDate !== undefined) {
      this.queryParams = {
        [endDateQueryParam]: this.endDate
      };
    }
    
    this.loadEvents();
    
  }

  public setStartDate = (event: Event) => {
    this.startDate = (event.target as HTMLInputElement).value;
  }

  public setEndDate = (event: Event) => {
    this.endDate = (event.target as HTMLInputElement).value;
  }
}
