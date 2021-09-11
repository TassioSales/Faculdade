import java.util.*;
public class BuscaLinear {

	public static void main (String[] args){
		
		int acumulador = 1;  //Um acumulador para gerar múltiplos de 3 no bloco a seguir
		int v[] = new int[10]; //Um vetor de 10 posições
		
		System.out.println("O vetor contém os seguintes valores:");
		
		/* Neste trecho do código, eu fiz um algoritimo simples que preenche automaticamente um vetor de 10
		 * posições. O intuito é livrar o usuário de digitar manualmente os valores
		 * será mostrado 
		 */
		
		for(int i = 0; i <= 9; i++){
			
			acumulador = i * 3;
			v[i] = acumulador;
			System.out.println(v[i]);
		}
		
		Scanner leitura = new Scanner(System.in);
		
		System.out.println("Digite o número a ser buscado no vetor:"); 
		int numero = leitura.nextInt(); //Número digitado pelo usuário para se comparado com os valores gerados no vetor acima.
		
		boolean bolFound = false; //Utilizou uma variável booleana que permite sinalizar se o valor foi ou não foi encontrado.
		int indFound = 0; //Variável que armazenará o valor do índice a qual se encontra o valor.
		
		/* Algoritimo bem direto e simples, comparo o valor que foi digitado com cada elemento do vetor (no caso de 0 a 9
		 * Caso encontre, a variável 'bolFound' se tornará verdadeira eo indice a qual foi encontrado será armazenado em 'indFound'
		 * Senpre lembrando que vetor em java se inicia do 0 (zero). Pode-ser fazer uma gambiarra para forçar ele iniciar do um,
		 * atribuindo logo na criação um valor qualquer para zero, e daí trabalhar com o vetor a partir do um. Se houver algum indice 
		 * do vetor 'vazio', o compilador indicará erro. Apesar que não testei essa idéia, numa próxima ocasião faço isto.
		 */
		for (int i = 0; i <= 9; i++){
			if (v[i] == numero){
				bolFound = true;
				indFound = i;
			}
			
		}
		
		/*Esse bloco cuida de mostrar se o valor foi encontrado ou não. Isso tudo depende do valor de bolFound. Caso resulte em
		 * true no bloco acima, então ele dirá que o valor foi encontrado no índice "tal"). Se foi 'sinalizado" falso, então dirá que 
		 * não foi encontrado
		 */
		
		if (bolFound)
		{
			System.out.println("O valor foi encontrado no índice " + indFound );
		}
		else
		{
			System.out.println("Valor não encontrado!");
		}
	}
}