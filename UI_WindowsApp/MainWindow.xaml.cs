using System;
using System.Net.Http;
using System.Threading.Tasks;
using System.Windows;

namespace UI_WindowsApp
{
    public partial class MainWindow : Window
    {
        private readonly HttpClient httpClient = new HttpClient();

        public MainWindow()
        {
            InitializeComponent();
        }

        private async void RunPipeline_Click(object sender, RoutedEventArgs e)
        {
            string disease = DiseaseInput.Text.Trim();
            if (string.IsNullOrEmpty(disease))
            {
                ResultBlock.Text = "Please enter a disease name.";
                return;
            }

            try
            {
                string apiUrl = $"http://localhost:8000/run_mcp_pipeline?disease={Uri.EscapeDataString(disease)}";
                var response = await httpClient.GetAsync(apiUrl);
                response.EnsureSuccessStatusCode();

                var json = await response.Content.ReadAsStringAsync();
                ResultBlock.Text = $"Final Compound Output:\n{json}";
            }
            catch (Exception ex)
            {
                ResultBlock.Text = $"Error: {ex.Message}";
            }
        }



    }
}