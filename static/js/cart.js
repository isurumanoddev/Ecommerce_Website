const updateBtns = document.getElementsByClassName("update-cart");

for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener("click", function () {
        const productId = this.dataset.product;
        const action = this.dataset.action;
        console.log("productId : ", productId, "action : ", action)
        console.log("User : ", user)

        if (user === "AnonymousUser") {

            console.log("user not sign in to website");
        } else {
            update_order(productId, action)

        }
    });
}

function update_order(productId, action) {
    console.log("user  log in , sending data......");

    const url = "/update_cart/"

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({"productId": productId, "action": action})
    })
        .then((response) => {
            return response.json()
        })
        .then((body) => {
            console.log("body : ", body)

        })

}

