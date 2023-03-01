const updateBtn = document.getElementsByClassName("update-cart");

for (let i = 0; i < updateBtn.length; i++) {
    updateBtn[i].addEventListener("click", function () {
        const productId = this.dataset.product
        const action = this.dataset.action
        console.log("productId : ", productId, "action :", action)
        console.log("USER :", user)
        if (user === "AnonymousUser") {
            console.log("Not Log In");
        } else {
            update_user_order(productId, action)
        }
    });
}

function update_user_order(productId, action) {
    console.log("user logged in,sending data....");

    let url = "/update_item/";

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({"productId": productId, "action": action}),
    })
        .then((response) =>{
            return response.json()
        })
        .then((data) => {
            console.log("data",data)
        })
}