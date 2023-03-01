const updateBtns = document.getElementsByClassName("update-cart");

for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener("click", function () {
        const productId = this.dataset.product
        const action = this.dataset.action
        console.log("productId  :", productId, "action :", action)

        console.log("user:", user)
        if (user === "AnonymousUser") {
            console.log("User not log in");
        } else {

            update_user_order(productId, action)
        }

    })
}

function update_user_order(productId, action) {
    console.log("User login, sending data...");

    const url = "/update_item/"

    fetch(url,{
        method: "POST",
        headers:{
            "Context-type": "application/json",
            "X-CSRFToken":csrftoken,
        },
        body:JSON.stringify({"productId":productId,"action":action}),
    })
        .then((response) =>{
            return response.json()
        })
        .then((data) =>{
            console.log("data",data)
        })
}