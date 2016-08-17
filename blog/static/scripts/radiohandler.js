

function ShowCheck() {
    if (document.getElementById('ext').checked) {      
		document.getElementById('extentions').style.display = 'block';
		document.getElementById('makeup').style.display = 'none';
		document.getElementById('brows').style.display = 'none';
		document.getElementById('nails').style.display = 'none';
		document.getElementById('hairdressings').style.display = 'none';
    }
    else if (document.getElementById('mup').checked) {
		document.getElementById('extentions').style.display = 'none';
		document.getElementById('makeup').style.display = 'block';
		document.getElementById('brows').style.display = 'none';
		document.getElementById('nails').style.display = 'none';
		document.getElementById('hairdressings').style.display = 'none';
	}
	else if (document.getElementById('br').checked) {
		document.getElementById('extentions').style.display = 'none';
		document.getElementById('makeup').style.display = 'none';
		document.getElementById('brows').style.display = 'block';
		document.getElementById('nails').style.display = 'none';
		document.getElementById('hairdressings').style.display = 'none';
	}
	else if (document.getElementById('nail').checked) {
		document.getElementById('extentions').style.display = 'none';
		document.getElementById('makeup').style.display = 'none';
		document.getElementById('brows').style.display = 'none';
		document.getElementById('nails').style.display = 'block';
		document.getElementById('hairdressings').style.display = 'none';
	}
	else if (document.getElementById('hair').checked) {
		document.getElementById('extentions').style.display = 'none';
		document.getElementById('makeup').style.display = 'none';
		document.getElementById('brows').style.display = 'none';
		document.getElementById('nails').style.display = 'none';
		document.getElementById('hairdressings').style.display = 'block';
	}
	else {
		document.getElementById('extentions').style.display = 'block';
		document.getElementById('makeup').style.display = 'block';
		document.getElementById('brows').style.display = 'block';
		document.getElementById('nails').style.display = 'block';
		document.getElementById('hairdressings').style.display = 'block';
	}
}