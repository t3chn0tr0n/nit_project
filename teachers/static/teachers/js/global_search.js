var loading = 0;
function autocomplete(inp, arr) {
  /*the autocomplete function takes two arguments,
    the text field element and an array of possible autocompleted values:*/
  var currentFocus;
  /*execute a function when someone writes in the text field:*/
  inp.addEventListener("input", function(e) {
    var a,
      b,
      i,
      val = this.value;
    /*close any already open lists of autocompleted values*/
    closeAllLists();
    if (!val) {
      return false;
    }
    currentFocus = -1;
    /*create a DIV element that will contain the items (values):*/
    a = document.createElement("DIV");
    a.setAttribute("id", this.id + "autocomplete-list");
    a.setAttribute("class", "autocomplete-items");
    /*append the DIV element as a child of the autocomplete container:*/
    this.parentNode.appendChild(a);
    /*for each item in the array...*/
    for (i = 0; i < arr.length-2; i+= 2) {
      console.log(arr[i+1]);
      /*check if the item starts with the same letters as the text field value:*/
      if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase() || arr[i + 1].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
        console.log("Hello");
        /*create a DIV element for each matching element:*/
        b = document.createElement("DIV");
        b.setAttribute("class", "border rounded row p-2");
        b.setAttribute("style", "width: 99%");
        b.setAttribute("align", "left");
        /*make the matching letters bold:*/
        b.innerHTML =
          "<span class='col-10 mx-auto small'><strong class='text-primary mt-1'>" +
          arr[i].substr(0, val.length) +
          "</strong>" +
          arr[i].substr(val.length) + "&nbsp;&nbsp;&nbsp;" +
          arr[i + 1].toUpperCase() + 
          "</span>";
          
        /*insert a input field that will hold the current array item's value:*/
        b.innerHTML +=
          "<input type='hidden' value='" +
          arr[i] + 
          "'> <span class='col-2 mx-auto'>"+"<a href='view_student/" + arr[i] + "'class='btn btn-sm btn-outline-primary mt-1'>view</a></span>" +
          "   ";
        /*execute a function when someone clicks on the item value (DIV element):*/
        b.addEventListener("click", function(e) {
          /*insert the value for the autocomplete text field:*/
          inp.value = this.getElementsByTagName("input")[0].value;
          /*close the list of autocompleted values,
                (or any other open lists of autocompleted values:*/
          closeAllLists();
        });
        a.appendChild(b);
      }
    }
  });
  /*execute a function presses a key on the keyboard:*/
  inp.addEventListener("keydown", function(e) {
    var x = document.getElementById(this.id + "autocomplete-list");
    if (x) x = x.getElementsByTagName("div");
    if (e.keyCode == 40) {
      /*If the arrow DOWN key is pressed,
          increase the currentFocus variable:*/
      currentFocus++;
      /*and and make the current item more visible:*/
      addActive(x);
    } else if (e.keyCode == 38) {
      //up
      /*If the arrow UP key is pressed,
          decrease the currentFocus variable:*/
      currentFocus--;
      /*and and make the current item more visible:*/
      addActive(x);
    } else if (e.keyCode == 13) {
      /*If the ENTER key is pressed, prevent the form from being submitted,*/
      e.preventDefault();
      if (currentFocus > -1) {
        /*and simulate a click on the "active" item:*/
        if (x) x[currentFocus].click();
      }
    }
  });
  function addActive(x) {
    /*a function to classify an item as "active":*/
    if (!x) return false;
    /*start by removing the "active" class on all items:*/
    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = x.length - 1;
    /*add class "autocomplete-active":*/
    x[currentFocus].classList.add("autocomplete-active");
  }
  function removeActive(x) {
    /*a function to remove the "active" class from all autocomplete items:*/
    for (var i = 0; i < x.length; i++) {
      x[i].classList.remove("autocomplete-active");
    }
  }
  function closeAllLists(elmnt) {
    /*close all autocomplete lists in the document,
      except the one passed as an argument:*/
    var x = document.getElementsByClassName("autocomplete-items");
    for (var i = 0; i < x.length; i++) {
      if (elmnt != x[i] && elmnt != inp) {
        x[i].parentNode.removeChild(x[i]);
      }
    }
  }
  /*execute a function when someone clicks in the document:*/
  document.addEventListener("click", function(e) {
    closeAllLists(e.target);
  });
}

$(document).ready(function() {
  $("input").keyup(function() {
    var srch = document.getElementById("search").value;
    if (srch.length >= 3) {
      /* to start the preloader */
      if (loading == 0) {
        var para = document.createElement("div");
        para.className = "loader";
        var element = document.getElementById("innr");
        element.appendChild(para);
        loading = 1;
      }
      /* end of preloader */
      $.ajax({
        type: "POST",
        url: "search_filter/",
        data: {
          srch: srch,
          csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
        },
        success: function(ids) {
          loading = 0;
          setTimeout(function() {
            $(".loader").remove();
          }, 0000);

          ids = ids.split("$");
          console.log(ids);
          autocomplete(document.getElementById("search"), ids);
        }
      });
    }
  });
});
