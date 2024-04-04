const searchField = document.querySelector("#search_idan");

const identityh = document.querySelector("#identity");

const identity_2h = document.querySelector("#identity_2");

const innerh = document.querySelector("#inner");

identity_2h.style.display = "none";


searchField.addEventListener("keyup", (e) => {
  const searchValue = e.target.value;

  if (searchValue.trim().length > 0) {
   
    innerh.innerHTML = "";
    fetch("/search/", {
      body: JSON.stringify({ searchText: searchValue }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("data", data);
        identityh.style.display = "none";
        identity_2h.style.display = "block";

        console.log("data.length", data.length);

        if (data.length === 0) {
          identityh.style.display = "block";
          identity_2h.style.display = "none";
        } else {
          
          data.forEach((item) => {
            innerh.innerHTML += `
               <a href="/care/phar/${item.id}/>
                <p>${ item.name }</p>
                <p>${ item.title }</p>
                <a/>`;
          });
        }
      });
  } else {
    identity_2h.style.display = "none";
    identityh.style.display = "block";
    
  }
});
