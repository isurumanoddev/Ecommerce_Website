const updateBtns = document.getElementsByClassName("update-cart");

for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener("click", function () {
        const productId = this.dataset.product;
        const action = this.dataset.action;
        console.log("productId : ", productId, "action : ", action)
        console.log("User : ", user)

        if (user === "AnonymousUser") {
            addCookieItem(productId, action)

        } else {
            update_order(productId, action)

        }
    });
}

/*function addCookieItem(productId, action) {
    console.log("user not sign in to website...");
    if (action === "add") {
        if (cart[productId] === undefined) {
            cart[productId] = {"quantity": 1};
        } else {
            cart[productId]["quantity"] += 1
        }

    }
    if (action === "remove") {
        cart[productId]["quantity"] -= 1

        if (cart[productId]["quantity"] <= 0) {
            console.log("remove idem")
            delete cart[productId]
        }
    }
    console.log("cart_cookie : ", cart)
    document.cookie = "cart_cookie" + JSON.stringify(cart) + ";domain=;path=/"

}*/

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
            window.location.reload()

        })

}

