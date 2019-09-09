import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PushbackReader;

public class Lexico {
	
	//Stream de leitura do arquivo-fonte
	PushbackReader r;
	
	//Lista de tokens
	ArrayList<Token> lt = new ArrayList<Token>();
	
	//Armazena código do caracter lido
	int intch;
	
	//Armazena código do caracter lido
	char ch;
	char ch1;
	char ch2;
	int linha = 1;
	
	int coluna = 1;
	
	
	public ArrayList<Token> analisa(String arquivo) throws IOException{
		
		//PushbackReader será usado para devolver caracter ao stream
		r = new PushbackReader (
			new BufferedReader(
					new InputStreamReader(
						new FileInputStream(arquivo), "US-ASCII")));
		
		while((intch = r.read()) != -1) {
			
			ch = (char) intch;
			System.out.println(ch);
			
			//Verificar se o ch é uma letra
			if(Character.isLetter(ch)) {
				System.out.println("É Letra");
			}
			
			//Verificar se o ch é um digito
			if(Character.isDigit(ch)) {
				System.out.println("É Digito");
			}
			
			//Verificar se o ch é uma Quebra de linha
			if(ch == '\n') {
				linha++;
				coluna = 1;
			}
			
			//Verifica se ch é um Operador Aritmético
			if(ch == '%' || ch == '/' || ch == '*' || ch == '+' || ch == '-') {
				System.out.println("É Operador Aritmético");
				continue;
			}
			
			//Verifica se ch é uma Atribuição
			if(ch == ':' || ch == '=') {
				if(ch == ':') {
					ch1 = ch;
				}else if(ch == '=') {
					ch2 = ch;
				}
				if( ("" + ch1 + ch2).equals(":=")) {
					System.out.println("É Atribuição");
					continue;
				}
			}
			
			//Verifica se ch é Relacional
			if(ch == '=' || ch == '<' || ch == '>' || ch == '!') {
				if(ch == '!' || ch == '=') {
					if(ch == '!') {
						ch1 = ch;						
					}else if(ch == '=') {
						ch2 = ch;
					}
					if( ("" + ch1 + ch2).equals("!=")) {
						System.out.println("É Relacional");
						continue;
					}
				}
				if(ch == '<' || ch == '=') {
					if(ch == '<') {
						ch1 = ch;						
					}else if(ch == '=') {
						ch2 = ch;
					}
					if( ("" + ch1 + ch2).equals("<=")) {
						System.out.println("É Relacional");
						continue;
					}
				}
				if(ch == '>' || ch == '=') {
					if(ch == '>') {
						ch1 = ch;						
					}else if(ch == '=') {
						ch2 = ch;
					}
					if( ("" + ch1 + ch2).equals(">=")) {
						System.out.println("É Relacional");
						continue;
					}
				}
				if(ch == '=') {
					if(ch == '=') {
						ch1 = ch;						
					}else if(ch == '=') {
						ch2 = ch;
					}
					if( ("" + ch1 + ch2).equals("==")) {
						System.out.println("É Relacional");
						continue;
					}
				}
				
			}
			
			//Verifica se ch é Pontuação
			if(ch == ';' || ch == ':' || ch == '.' || ch == ',' || ch == '(' || ch == ')' || ch == '{' || ch == '}' || ch == '[' || ch == ']' || ch == '!' || ch == '?') {
				System.out.println("É Pontuação");
				continue;
			}
		}
		
		return lt;
		
	}
	
}
