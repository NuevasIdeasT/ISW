import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-membrecia',
  templateUrl: './membrecia.component.html',
  styleUrls: ['./membrecia.component.css']
})
export class MembreciaComponent implements OnInit {

  numero:number;
  constructor() {
    this.numero=11;
  }

  ngOnInit() {
  }

  change(num:number)
  {
    console.log(num);
    this.numero=num;
  }

}
