

function init() {
    let arg = `.products-container`
    alert("ok")
    apiGetAllProducts().then((response) => {
        showProducts(response, arg)
        handleAddProductClick()
    })
}

init();

export function showProducts(products, arg) {
    const products_container = document.querySelector(arg)
    console.log("products: " + products[0])
    console.log("container: " +products_container)
    products_container.innerHTML = "";
    for (let product of products) {
        let imgPath = `/product_${product.id}.jpg`
        products_container.insertAdjacentHTML("beforeend", `
                                            <a href="/product/${product.id}">
                                                <div class="product-card"  >
                                                    <img class="product-image" src="/static/images${imgPath}" alt=""> 
                                                    <div class="card-header">
                                                        <h4>${product.name}</h4> 
                                                        <p class="card-text">${product.description} </p>                                           
                                                    </div>
                                                    <div class="card-body">
                                                        <div class="card-text">
                                                            <p class="lead">${product.actual_price}</p>
                                                        </div>
                                                        <div class="card-text">
                                                            <button id="${product.id}" class="btn btn-success btn-add-product" >Add to cart</button>
                                                        </div>
                                                    </div>
                                                </div>
                                            </a>
                                            
                                            
                                            `)
    }
}

export async function apiUpdateCart(product_id, quantity) {
    let url = `/api_update_cart/${product_id}/${quantity}`
    const products = await apiPut(url, {"product_id": product_id, "quantity": quantity})
    return products
}


export async function apiGetAllProducts() {
    let category_id = 0
    let supplier_id = 0
    let url = `/api_get_products/${category_id}/${supplier_id}`
    const products =  await apiGet(url, {"category_id": category_id, "supplier_id": supplier_id})
    return products;
}

export function handleAddProductClick() {
    const addButtons = document.querySelectorAll(`.btn-add-product`)
    addButtons.forEach(button => {
        button.addEventListener("click", () => {
            apiUpdateCart(button.id, 1)
        })
    })

}

async function apiGet(url) {
    let response = await fetch(url, {
        method: "GET",
    })
    if (response.status === 200) {
        let data = response.json()
        return data
    }
}

async function apiPost(url, payload) {
    let response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    })
    if (response.ok) {
        let data = response.json()
        return data
    }
}

async function apiDelete(url, payload) {
    let response = await fetch(url, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    })
    if (response.ok) {
        let data = response.json()
        return data
    }
}

async function apiPut(url, payload) {
    let response = await fetch(url, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    })
    if (response.ok) {
        let data = response.json()
        return data
    }
}

