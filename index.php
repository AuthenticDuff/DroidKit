<style>
div.Title {
	font-family:"Trebuchet MS", Arial, Helvetica, sans-serif;
	font-size: 28px;
	color:#000080;
	text-align: center;
  	margin-top: 20px;
  	margin-left: 5px;
}

div.Table2 {
	font-family:Arial, Helvetica, sans-serif;
	text-align: center;
  	margin-top: 20px;
  	margin-left: 5px;
	color:#000080;
}


div.fullscreen-bg {
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    overflow: hidden;
    z-index: -100;
}

div.fullscreen-bg__video {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}


@media (min-aspect-ratio: 16/9) {
  .fullscreen-bg__video {
    height: 300%;
    top: -100%;
  }
}

@media (max-aspect-ratio: 16/9) {
  .fullscreen-bg__video {
    width: 300%;
    left: -100%;
  }
}


.Form {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translateX(-50%) translateY(-50%);
}
	
	
.logo {
    height: 25px;
    width: 300px;
    display: block;
    margin-left: auto;
    margin-right: auto;
}




</style>

<script src='https://www.google.com/recaptcha/api.js'></script>

<div class="fullscreen-bg">
    <video loop muted autoplay poster="img/videoframe.jpg" class="fullscreen-bg__video">
        <source src="video/videobackground.mp4" type="video/mp4">
    </video>
</div>

<div class="Title">
<h1> Please Sign Up To Continue </h1>
</div>


<div class="logo">
<img src="../../Experimentation with PHP/SignUp Page/logo.png" alt="Logo here" width="400" height="200" />
</div>

<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />


<link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/themes/smoothness/jquery-ui.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js"></script>
  
  <script>
  $(document).ready(function() {
    $("#datepicker").datepicker();
  });
  </script>
  
  
<script>
document.getElementById('bio').style.height="200px";
</script>


<div class="table2">
  <form action="../../Experimentation with PHP/SignUp Page/submitinfo.php" method="post">
  <table style="width: 50%" align="center">
  <tr>
        <td>
  <p>Username:</p>
        </td>
        <td>
  <input type="text" name="username" required="required">
        </td>
  </tr>
  <tr>
        <td>
  <p>Today's date:</p>
        </td>
        <td>
  <input id="datepicker" name="signupdate" required="required">
        </td>
  </tr>
  <tr>
        <td>
  <p>Email:</p>
        </td>
        <td>
  <input type="email" name="email" required="required">
        </td>
  </tr>
        <td>
  <p>Bio:</p>
        </td>
        <td>
  <input style="height:200px;font-size:14pt;" type="text" name="bio" required="required">
        </td>
  </tr>
        <td>
  <p>Gender:</p>
        </td>
        <td>
  <select name="gender"><option value="male">Male</option> <option value="female">Female</option></select>
        </td>
  </tr>
  <tr>
        <td colspan="2">
        <div class="g-recaptcha" data-sitekey="6Lf6hCQTAAAAANuf7JkAlPjAXwZTx_mYe4vbeaNB"> </div>
        </td>
        </tr>
        <tr>
        <td colspan="2">
 		<input type="submit" style="height:200px;width:200px;color:#39F" onclick="submitform()" value="Submit" />
        </td>
  </tr>  
  </table>
  </form>
</div>