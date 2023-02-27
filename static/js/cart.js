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
            console.log("success");
        }
    });
}


