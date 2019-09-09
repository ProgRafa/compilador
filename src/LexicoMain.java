import java.io.IOException;
import java.util.ArrayList;

public class LexicoMain {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

//		Cria lista de tokens
		ArrayList<Token> lt = new ArrayList<Token>();
		
//		Cria analisador Léxico
		Lexico lexico = new Lexico();
		
//		Realiza a analise lexica
//		lexico.analisa(args[0]);
		lt = lexico.analisa("teste1.lpd");
		
//		Imprime número de tokens
		System.out.println("Numero de tokens: "+lt.size());
		
//		Percorre a lista de tokens imprimindo-os
		lt.forEach(token -> System.out.println(token.toString()));
		
	}

}
