setPreferences();

/* <<< EVENTS >>> */
function navbarOpenTab(event,tab){clearClassLists('.navbar a','active');event.currentTarget.classList.add("active");openTab(event, tab);}
function openTab(event,tab){setInnerToElement("mainTab",tab);window.scroll(0, 0);event.preventDefault();}
function openTabSide(event,tab){setInnerToElement("articleTab",tab);clearClassLists('.sidebar li','active');event.currentTarget.classList.add('active');event.preventDefault();}
function sidebarOpenUl(event,id){clearClassLists('.sidebar li','active');event.currentTarget.classList.add('active');displayChange(id);}
/* <<< ------ >>> */

/* <<< GENERAL >>> */
function displayChange(id){document.getElementById(id).style.display=document.getElementById(id).style.display==="none"?"block":"none";}
function clearClassLists(selector,classItem){const links=document.querySelectorAll(selector);links.forEach(link=>link.classList.remove(classItem))}
async function setInnerToElement(id, page){document.getElementById(id).innerHTML = await getPage(page);}
async function getPage(page){try{const response=await fetch(page);if(!response.ok)throw new Error('HTTP error '+response.status);return await response.text()}catch(error){console.error('Error fetching page:',error);return null}}
/* <<< ------- >>> */

function onSubBtnClick(event) {
    swapSubMenuLook(event.currentTarget.parentNode.querySelector('.submenu'));
    event.currentTarget.querySelector('ion-icon').classList.toggle('open');
}

function onSubitemClick(event, page) {
    clearClassLists('.sidebar li', 'active')
    event.currentTarget.classList.add('active');
    setInnerToElement('articleTab', page);
    window.scrollTo(0,0);
}

function swapSubMenuLook(target) {
    target.classList.toggle('show');
}

/* <<< LOAD >>> */
function setPreferences() {
    window.onbeforeunload=function(){window.scrollTo(0,0);};
    var menu = document.querySelector('header').querySelector('.main').querySelector('.menu');
    var navbar = document.querySelector('.navbar');
    menu.onclick=()=>{ navbar.classList.toggle('open');}
    setInnerToElement("mainTab",'main');
}
/* <<< ---- >>> */
