<!DOCTYPE html>
<html>
<head>
  <title>Gallery - {{search_text}}</title>

  <link rel="stylesheet" type="text/css" href="/static/style.css" />
  <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
  <script type="text/javascript" src="/static/jquery.masonry.min.js"></script>
</head>

<body>
  <div id="container">
    <form method="POST" action="/search">
      DigitalNZ image search: <input name="search" type="text" class="big-text" />
      <input type="submit" class="big-text" />
    </form>

    <h3>Results for "{{search_text}}"</h3>

    %prev = int(page) - 1
    %next = int(page) + 1

    <p>This is page {{page}}. <a href="{{prev}}">Previous</a>. <a href="{{next}}">Next</a>.</p>
    <div id="gallery-container">
      <ul id="gallery">
        %for row in data:
        <li class='item'><a href="http://digitalnz.org/records/{{row['id']}}"><img src="{{row['thumbnail_url']}}" class='thumb' /></a></li>
        %end

      </ul> 
    </div>
    <div>This is page {{page}}. <a href="{{prev}}">Previous</a>. <a href="{{next}}">Next</a>.</div>
    
  </div>

  <script>
  var $container = $('#gallery');
  $container.imagesLoaded(function(){
    $container.masonry({
      itemSelector : '.item',
      columnWidth : 240
    });
  });
  </script>

</body>
</html>