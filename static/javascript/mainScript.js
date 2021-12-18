

homePageScript();

function homePageScript() {
    const arg = `.products-container`
    const categorySelector = document.querySelector(`#categorySorter`)
    const supplierSelector = document.querySelector(`#supplySorter`)
    try {
        categorySelector.addEventListener("change", () => {
            apiGetAllProducts(categorySelector.value, supplierSelector.value).then((response) => {
                showProducts(response, arg)
            })
        })


        supplierSelector.addEventListener("change", () => {
        apiGetAllProducts(categorySelector.value, supplierSelector.value).then((response) => {
            showProducts(response, arg)
        })
    })


        apiGetAllProducts(categorySelector.value, supplierSelector.value).then((response) => {
        showProducts(response, arg)
        handleAddProductClick()
    })
    } catch (e) {

    }




}
//
// export function cartPageScript() {
//     const arg = `.products-container`
//     apiGetCart().then(response => {
//         showCartProducts(response, arg)
//         handleAddProductClick()
//     })
// }

export function productsPageScript() {
    const arg = `.products-container`
    apiGetAllProducts(0, 0).then((response) => {
        showProducts(response, arg)
        handleAddProductClick()
    })
}


export function showProducts(products, arg) {
    const products_container = document.querySelector(arg)
    console.log("products: " + products[0])
    console.log("container: " +products_container)
    products_container.innerHTML = "";
    for (let product of products) {
        let imgPath = `/product_${product.id}.jpg`
        let firstPart = `<div class="product-card"  >
                                                    
                                                    <img class="product-image" src="/static/images${imgPath}" alt=""> 
                                                        <a href="/product/${product.id}">
                                                            <div class="card-header">
                                                                <h4>${product.name}</h4> 
                                                                                                           
                                                            </div>
                                                        </a>
                                                    <div class="card-body">
                                                        <div class="card-text">`
        let secPart = `<h1 class="lead price">${product.actual_price} Lei</h1>
                                                        </div>
                                                        <div class="card-text">
                                                            <button id="${product.id}" class="btn btn-success btn-add-product" >Add to cart</button>
                                                        </div>
                                                    </div>
                                                </div>`
        let optional = `<p class="lead"><strike>${product.default_price} Lei</strike></p>`
        if (product.actual_price !== product.default_price) {
            firstPart = firstPart + optional + secPart
        } else {
            firstPart += secPart
        }

        products_container.insertAdjacentHTML("beforeend",firstPart)
    }
}



export async function apiUpdateCart(product_id, quantity) {
    let url = `/api_update_cart/${product_id}/${quantity}`
    const products = await apiPut(url, {"product_id": product_id, "quantity": quantity})
    return products
}

export async function apiGetCart() {
    let url = `/api_get_cart`
    const products = await apiGet(url)
    return products
}


export async function apiGetAllProducts(category_id, supplier_id) {

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

