const deleteButton = document.getElementById("deleteID");

deleteButton.addEventListener("mouseout", function(){
    this.textContent = `😔\nDeletar`;
});

deleteButton.addEventListener("mouseover", function(){
    this.textContent = `😭\nDeletar`;
});

const cancelButton = document.getElementById("cancelID");

cancelButton.addEventListener("mouseout", function(){
    this.textContent = `🥺\nCancelar`;
});

cancelButton.addEventListener("mouseover", function(){
    this.textContent = `😀\nCancelar`;
});