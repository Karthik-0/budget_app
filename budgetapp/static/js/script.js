
    document.querySelector('#categoryInput').addEventListener('keydown',function(e){
       
        if(e.keyCode != 13){
            // console.log("hello")
            return;
        }
        else{
        e.preventDefault() 
            // console.log("hniu")
        var categoryname = this.value
        // console.log("Ere",categoryname)
        this.value = ''
        addnewCategory(categoryname)
        updateCategoryString()
        }
    })

    function addnewCategory(name){
        document.querySelector("#categoriesContainer").insertAdjacentHTML('beforeend',
        `
        <li class="category mt-2">
        <span class="name">${name}</span>
        <span onclick="removeCategory(this)" class="text-danger font-weight-bold">x</span>
    </li>
        `
    )
    }
    function fetchCategoryArray(){
        var categories = []
        document.querySelectorAll('.category').forEach(function(e){
            // console.log("quer ",e)
            name = e.querySelector('.name').innerHTML
            // console.log("name = ",name)
            if(name == '') return;
            categories.push(name);

        })

        return categories
    }

    function updateCategoryString(){
        categories = fetchCategoryArray()
        document.querySelector('input[name="categoryString"]').value = categories.join(',')
    }


function removeCategory(e){
    e.parentElement.remove()
    updateCategoryString()
}