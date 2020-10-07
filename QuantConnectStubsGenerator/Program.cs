using System;
using System.IO;
using System.Reflection;
using log4net;
using log4net.Config;

namespace QuantConnectStubsGenerator
{
    internal static class Program
    {
        private static readonly ILog Logger = LogManager.GetLogger(typeof(Program));

        private static void Main(string[] args)
        {
            XmlConfigurator.Configure(
                LogManager.GetRepository(Assembly.GetEntryAssembly()),
                new FileInfo("log4net.config"));

            if (args.Length != 2)
            {
                Logger.Error("Usage: dotnet run <Lean directory> <output directory>");
                Environment.Exit(1);
            }

            try
            {
                new Generator(args[0], args[1]).Run();
            }
            catch (Exception e)
            {
                Logger.Error("Generator crashed", e);
                Environment.Exit(1);
            }
        }
    }
}
