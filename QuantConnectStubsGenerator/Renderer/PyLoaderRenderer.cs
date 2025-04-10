/*
 * QUANTCONNECT.COM - Democratizing Finance, Empowering Individuals.
 * Lean Algorithmic Trading Engine v2.0. Copyright 2014 QuantConnect Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
*/

using System.IO;

namespace QuantConnectStubsGenerator.Renderer
{
    public class PyLoaderRenderer : BaseRenderer
    {
        public PyLoaderRenderer(TextWriter writer) : base(writer)
        {
        }

        public void Render(string ns)
        {
            var baseNamespace = ns.Split(".")[0];
            var assembly = ns == "QuantConnect" ? "QuantConnect.Common" : ns;

            WriteLine($@"
import os
import sys

# If quantconnect-stubs is installed via pip and Lean is ran locally,
# importing anything from the current namespace makes the Python
# interpreter look in the quantconnect-stubs package for the implementation.
#
# The desired behavior is for the interpreter to use the implementation
# provided by the AddReference() call from Python.NET.
#
# To fix this, we temporarily remove the directory containing the
# quantconnect-stubs package from sys.path and re-import the current namespace
# so the relevant C# namespace is used when running Lean locally.

# Find the directory containing quantconnect-stubs (usually site-packages)
current_path = os.path.dirname(__file__)
while os.path.basename(current_path) != ""{baseNamespace}"":
    current_path = os.path.dirname(current_path)
current_path = os.path.dirname(current_path)

# Temporarily remove the directory containing quantconnect-stubs from sys.path
original_path = sys.path[:]
sys.path.remove(current_path)

# Import the C# version of the current namespace
del sys.modules[""{ns}""]
from clr import AddReference
AddReference(""{assembly}"")
from {ns} import *

# Restore sys.path
sys.path = original_path
            ".Trim());
        }
    }
}
