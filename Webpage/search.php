<!DOCTYPE html>
<html>
<head>
  <title>Jetstrap - The Bootstrap Interface Builder</title>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="keywords" content="Bootstrap,Twitter Bootstrap,Mockup,Builder,Interface Builder,CSS Framework,Drag and drop,WYSIWYG,Codiqa,Drifty,Twitter">
  <meta name="description" content="Rapid interface builder for Twitter Bootstrap. Generates real Bootstrap HTML, CSS, and Javascript. Easy and fast!">

  <meta property="og:title" content="Jetstrap: The Twitter Bootstrap Builder Tool" />
  <meta property="og:url" content="https://jetstrap.com/" />
  <meta property="og:site_name" content="Jetstrap for Bootstrap" />
  <meta name="og:description" content="Rapid interface builder for Twitter Bootstrap. Generates real Bootstrap HTML, CSS, and Javascript. Easy and fast!" />
  <meta property="og:type" content="website" />
  <meta property="og:image" content="http://jetstrap-site.s3.amazonaws.com/images/social/twitter.png" />

  <link rel="stylesheet" href="https://s3.amazonaws.com/jetstrap-site/css/normalize.css" type="text/css" />
  <link rel="stylesheet" href="https://s3.amazonaws.com/jetstrap-site/lib/bootstrap/css/bootstrap.min.css" />
  <link rel="stylesheet" href="template.css" />
  <link rel="stylesheet" href="https://s3.amazonaws.com/jetstrap-site/css/common.css?3" type="text/css" />
  <link rel="icon" href="https://s3.amazonaws.com/jetstrap-site/images/common/jetstrap_favicon.png" />
  
<link rel="stylesheet" href="https://s3.amazonaws.com/jetstrap-site/lib/hellobar/hellobar.css">
<style>
  body {
  }
  header {
      height: 80px;
  }
  #hellobar-container {
    box-shadow: none;
    -moz-box-shadow: none;
    -webkit-box-shadow: none;
  }
      .container{
      margin-top:20px;
      vertical-align: middle;

    }
    .form-group{
      display: table;
      margin: 0 auto;
      float:left
    }
</style>
  <style>
    header {
    }
    #content-wrapper {
      padding-top: 60px;
    }
    #ionic-header a {
      color: #fff;
      text-decoration: underline;
    }
  
    @media only screen and (min-width: 768px) {
        /* tablets and desktop */
    }
    
    @media only screen and (max-width: 400px) {
      header {
        position: absolute;
      }
      .grid-row [class*="grid"] {
        float: none !important;
        margin: 0px;
        margin-bottom: 20px;
        width: 100% !important;
        max-width: 100% !important;
      }
    }
    @media only screen and (max-width: 767px) {
        /* phones */
      #index .details .icons {
        margin: auto;
        float: none;
      }
      #hellobar-container > * {
        overflow: hidden;
      }
      .wrapped-content {
        width: 100%;
      }
      #cta-content .wrapped-content {
        padding-top: 90px;
      }
      #cta-content .bottom {
        width: 100%;
        margin-top: 15px;
      }
      header a.link {
        margin-right: 5px;
      }
      .grid-row [class*="grid"] {
        float: left;
        margin-left: 10px;
      }
      .grid-row {
        width: 100%;
        max-width: 100%;
      }
      .grid-row .grid-3 {
        max-width: 30%;
      }
    }
    @media only screen and (max-width: 767px) and (orientation: portrait) {
        /* portrait phones */
    }
  </style>
</head>
<body>
  <header class="">

    <div class="wrapped-content">
      <div class="l">
        <a href="/#top" class="jetstrap-logo"></a>
      </div>
      <div class="r">
        <a href="link to the search page here" class="link" target="_blank">Search</a>
        
        <a id="header-login-button" href="#login-modal" role="button" data-toggle="modal" class="button flat-blue-button no-right-border">Log in</a><a href="/plans" class="button flat-gray-button no-left-border">Sign up</a>
        
      </div>
    </div>
  </header>
  <div id="content-wrap">
    
<div id="fb-root"></div>


<a name="search"></a>
<div class="container">
    <div class="row">
        <div  class="form-group" style="text-align:center;margin-left:10%">Input quantity<br><input id="unitvalue" type="text" class="form-control" placeholder="Quantity"></br></div>
        <div class="bs-docs-example" style="float:left;text-align:center;margin-left:5px">
        Units of interest
        <br>
          <select id="units" class="row-fluid" title='units' data-width="50px" >
              <option>pieces</option>
              <option>liters</option>
              <option>kilos</option>
          </select>
          </br>
        </div>

        <div class="form-group" style="float:left;text-align:center;margin-left:5px">Key words of interest<br><input id="keywords" type="text" class="form-control" placeholder="Key words"></br></div>
        <div class="bs-docs-example" style="float:left;text-align:center;margin-left:5px">
        Region of interest
        <br>
          <select id="region" class="row-fluid" title='regions' data-title='regions' data-width="75%">
          <optgroup label="Europe">
              <option>West Europe</option>
              <option>East Europe</option>
              <option>Russia</option>
              <option>South Europe</option>
          <optgroup label="Asia">
              <option>West Asia</option>
              <option>East Asia</option>
              <option>South Asia</option>
              <option>South Asia Islands</option>
          <optgroup label="Africa">
              <option>North Africa</option>
              <option>South Africa</option>
          <optgroup label="America">
              <option>Caribbean Islands</option>
              <option>Central America</option>
              <option>North America</option>
              <option>South America</option>
          <optgroup label="Misc">
              <option>Australia</option>
              <option>New Zealand</option>
          </select>
          </br>
          </div>
      <button id="search" type="submit" class="btn btn-default" style="float:left;margin-top:20px;margin-left:5px">Search</button>
  </div>
</div>


  

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
  <script src="https://s3.amazonaws.com/jetstrap-site/lib/underscore-min.js"></script>
  <script src="https://s3.amazonaws.com/jetstrap-site/lib/backbone-min.js"></script>
  <script src="https://s3.amazonaws.com/jetstrap-site/lib/bootstrap_custom/js/bootstrap.min.js"></script>
  <script type="text/javascript">
  $(document).ready(function() {
  // Function to get input value.
  $('#search').click(function() {
  var unitvalue = $("#unitvalue").val();
  var unit= $('#units').val();
  var region= $('#region').val();
  var keywords= $('#keywords').val();
  if(unitvalue=='' || $.isNumeric(unitvalue)==false) {
  alert("Enter an Integer In Input Field");
  }else{
  alert(unitvalue+unit+region+keywords);
  }
  });

});
  </script>
</body>
</html>