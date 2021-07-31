  .baselayer{

      
    }
    .body {
      height: 100%;
      width: 100%;
      margin: 0px;
    }

    .textbox {
      width: 200px;
      height: 80%;
      background-color: blanchedalmond;
      display: flex;
      flex-direction: column;
      justify-content: space-around;
      border: 3px solid darkseagreen;
      border-radius: 60px;
      margin-top: 100px;
      margin-bottom: 100px;
      margin-right: 150px;
      margin-left: 80px;
    }

    .title {

      background-color: aquamarine;
      font-size: 8;
      text-align: center;
      font-family: 'Indie Flower', cursive;

      border-radius: 20px;


    }

    .floatbox {
      background-color: antiquewhite;
      /* background-opacity: 60%; */
      float: left;
      max-width: 60%;
      max-height: 45%;
      margin-top: 10%;
    }

    #rantbox {
      resize: none;
      width: 90%;
    }

    .menu {
      visibility: hidden;
    }

    button+.menu:active,
    button:focus+.menu {
      visibility: visible;
    }

    .bar {
      border: 3px solid darkseagreen;
      border-radius: 60px;
      background-color: honeydew;
      padding-left: 10px;
      padding-right: 10px;
      padding-top: 20px;
      padding-bottom: 20px;
      margin-top: 100px;
      display: block;
    }



    .form {
      display: flex;
      flex-direction: column;
      height: 800px;
      justify-content: space-between;
    }

    .list {
      background-color: rgb(199, 199, 238);
      height: 100px;
      width: 100px;
      display: flex;
      flex-direction: column;
    }

    .container {
      margin: 0px;
      display: flex;
      align-items: stretch;
      /* align-content: center; */
      justify-content: space-around;
      width: 100%;
      background-color: burlywood;
      height: 80%;

    }

    .box {
      margin-top: 10px;
      background-color: beige;
      height: 15%;
      border-radius: 60px;
      border: 3px solid blueviolet;
      width: 30%;
      padding-left: 10px;
      padding-right: 10px;

      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }

    .col {
      background-color: rgb(33, 36, 211);

      display: flex;
      flex-direction: column;
      width: 90%;
      justify-content: space-around;
      /* width: 40%; */

    }

   

    .logbook {
      border: 3px solid blueviolet;
      background-color: darksalmon;
      display: flex;
      flex-direction: row;
      justify-content: space-around;

    }


    .topbar {
      background-color: antiquewhite;
      display: block;
      height: 10%
    }

    .bottombar {
      background-color: white;
      border: 3px solid black;
      display: flex;
      align-items: center;
      justify-items: center;
      width: 100%;
      flex-direction: column
    }