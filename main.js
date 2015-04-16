$.getScript("/webiopi.js", function(){

	webiopi().ready(function() {
		var btm01 = webiopi().createGPIOButton(16, 'Sala');
		// var NomeBotao = webiopi().createGPIOButton(PINO, "INFO BOTAO");
		var btm02 = webiopi().createGPIOButton(18, 'Rua 01');
		var btm03 = webiopi().createGPIOButton(19, 'Rua 02');
		var btm04 = webiopi().createGPIOButton(20, 'Fundos');
		var btm05 = webiopi().createGPIOButton(21, 'Fotocélula');

		$("#btm01").append(btm01);
		// $("#ID da DIV").append(NomeBotao);
		$("#btm02").append(btm02);
		$("#btm03").append(btm03);
		$("#btm04").append(btm04);
		$("#btm05").append(btm05);

		webiopi().refreshGPIO(false);
		// Refresh
		//	TRUE = REPETIDAMENTE
		//	FALSE = UMA VEZ
	});
});