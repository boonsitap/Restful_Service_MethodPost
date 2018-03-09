import { Component } from '@angular/core';
import { NavController, NavParams } from 'ionic-angular';
import { HttpClient } from '@angular/common/http';

@Component({
    selector: 'page-main',
    templateUrl: 'main.html',
  })

export class MainPage {

    constructor(public navCtrl: NavController, public http: HttpClient) {
      this.postRequest();
    }

    postRequest() {
        let item = {
            id: 58364388
        }
        console.log("Student ID: 58364388")
        this.http.post("http://10.0.2.15:5500/api/id",item).subscribe(val => {
            console.log(val['item']); 
        });
    }
}