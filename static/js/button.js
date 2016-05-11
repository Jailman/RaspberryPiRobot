function turn_on()
{}

function turn_off()
{}

function changeImage()
{
element=document.getElementById('myimage')
if (element.src.match("on"))
  {
  element.src="/static/btimg/off.png";
  }
else
  {
  element.src="/static/btimg/on.png";
  }
}

