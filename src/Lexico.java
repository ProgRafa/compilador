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
	
	//Armazena c�digo do caracter lido
	int intch;
	
	//Armazena c�digo do caracter lido
	char ch;
	char ch1;
	char ch2;
	int linha = 1;
	
	int coluna = 1;
	
	
	public ArrayList<Token> analisa(String arquivo) throws IOException{
		
		//PushbackReader ser� usado para devolver caracter ao stream
		r = new PushbackReader (
			new BufferedReader(
					new InputStreamReader(
						new FileInputStream(arquivo), "US-ASCII")));
		
		while((intch = r.read()) != -1) {
			
			ch = (char) intch;
			System.out.println(ch);
			
			//Verificar se o ch � uma letra
			if(Character.isLetter(ch)) {
				System.out.println("� Letra");
			}
			
			//Verificar se o ch � um digito
			if(Character.isDigit(ch)) {
				System.out.println("� Digito");
			}
			
			//Verificar se o ch � uma Quebra de linha
			if(ch == '\n') {
				linha++;
				coluna = 1;
			}
			
			//Verifica se ch � um Operador Aritm�tico
			if(ch == '%' || ch == '/' || ch == '*' || ch == '+' || ch == '-') {
				System.out.println("� Operador Aritm�tico");
				continue;
			}
			
			//Verifica se ch � uma Atribui��o
			if(ch == ':' || ch == '=') {
				if(ch == ':') {
					ch1 = ch;
				}else if(ch == '=') {
					ch2 = ch;
				}
				if( ("" + ch1 + ch2).equals(":=")) {
					System.out.println("� Atribui��o");
					continue;
				}
			}
			
			//Verifica se ch � Relacional
			if(ch == '=' || ch == '<' || ch == '>' || ch == '!') {
				if(ch == '!' || ch == '=') {
					if(ch == '!') {
						ch1 = ch;						
					}else if(ch == '=') {
						ch2 = ch;
					}
					if( ("" + ch1 + ch2).equals("!=")) {
						System.out.println("� Relacional");
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
						System.out.println("� Relacional");
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
						System.out.println("� Relacional");
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
						System.out.println("� Relacional");
						continue;
					}
				}
				
			}
			
			//Verifica se ch � Pontua��o
			if(ch == ';' || ch == ':' || ch == '.' || ch == ',' || ch == '(' || ch == ')' || ch == '{' || ch == '}' || ch == '[' || ch == ']' || ch == '!' || ch == '?') {
				System.out.println("� Pontua��o");
				continue;
			}
		}
		
		return lt;
		
	}
	
}
